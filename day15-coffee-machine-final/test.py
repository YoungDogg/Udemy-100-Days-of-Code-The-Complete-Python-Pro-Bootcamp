import unittest
from unittest.mock import patch
from controller import check_resources, insert_coin, report, make_coffee
from config import MENU, resources

class TestController(unittest.TestCase):

    def setUp(self):
        # Set up initial resources for each test
        self.initial_resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.order = "latte"
        resources["water"] = self.initial_resources["water"]
        resources["milk"] = self.initial_resources["milk"]
        resources["coffee"] = self.initial_resources["coffee"]

    def test_check_resources(self):
        # Test when resources are sufficient
        self.assertTrue(check_resources(resources, self.order))

        # Test when resources are insufficient
        resources["water"] = 0
        self.assertFalse(check_resources(resources, self.order))

    @patch('builtins.input', side_effect=[10, 10, 10, 10])
    def test_insert_coin(self, mock_input):
        # Mocking input to simulate coin insertion
        self.assertEqual(insert_coin(), 4.1)  # Update expected result to 4.1

    def test_report(self):
        with patch('builtins.print') as mocked_print:
            report(money=10)
            mocked_print.assert_called_with(
                '\ncurrent resource values\nWater: 300\nMilk: 200\nCoffee: 100\nMoney: 10\n')

    def test_make_coffee(self):
        make_coffee(self.order)
        self.assertEqual(resources["water"], self.initial_resources["water"] - MENU[self.order]["ingredients"]["water"])
        self.assertEqual(resources["milk"], self.initial_resources["milk"] - MENU[self.order]["ingredients"]["milk"])
        self.assertEqual(resources["coffee"], self.initial_resources["coffee"] - MENU[self.order]["ingredients"]["coffee"])

if __name__ == '__main__':
    unittest.main()
