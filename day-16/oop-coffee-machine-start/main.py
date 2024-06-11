from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_working = True
while is_working:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_working = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        chosen_menu = menu.find_drink(choice)
        if chosen_menu:
            if coffee_maker.is_resource_sufficient(chosen_menu) and money_machine.make_payment(chosen_menu.cost):
                coffee_maker.make_coffee(chosen_menu)
            else:
                print("Sorry, we canno process your order.")