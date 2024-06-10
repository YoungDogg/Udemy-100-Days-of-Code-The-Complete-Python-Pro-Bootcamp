# test_control.py
import unittest
from unittest.mock import patch
from control import diff_check_of_b, answer_func, game_update
from game_data import data

class TestControl(unittest.TestCase):

    @patch('random.randint')
    def test_diff_check_of_b(self, mock_randint):
        mock_randint.side_effect = [0, 1]  # Mocking random indices
        a, b = diff_check_of_b()
        self.assertNotEqual(a, b)
        self.assertIn(a, data)
        self.assertIn(b, data)

    def test_answer_func(self):
        a = {"name": "A", "follower_count": 100}
        b = {"name": "B", "follower_count": 50}
        self.assertEqual(answer_func(a, b), a)
        self.assertEqual(answer_func(b, a), a)

        a = {"name": "A", "follower_count": 50}
        b = {"name": "B", "follower_count": 100}
        self.assertEqual(answer_func(a, b), b)
        self.assertEqual(answer_func(b, a), b)

    @patch('builtins.input', side_effect=['A', 'B'])
    @patch('control.diff_check_of_b', return_value=(data[0], data[1]))
    @patch('control.answer_func')
    def test_game_update(self, mock_answer_func, mock_diff_check, mock_input):
        mock_answer_func.return_value = 'A'
        with patch('builtins.print') as mocked_print:
            game_update()
            self.assertTrue(mocked_print.called)
            self.assertEqual(mock_input.call_count, 2)

if __name__ == '__main__':
    unittest.main()