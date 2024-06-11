from controller import check_resources, insert_coin, report, make_coffee
from config import MENU, resources

import os

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')


is_machine_working = True

while is_machine_working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if user_input == "off":
        clear()
        is_machine_working = False
        continue


    if user_input == "report":
        report()
        continue


    is_resourceful = check_resources(resources, user_input)
    memu_cost: int = MENU[user_input]["cost"]
    if not is_resourceful:
        print("please pick other drink")
        continue


    if is_resourceful:
        input_coin = insert_coin()


    # enough money
    if memu_cost <= input_coin:
        report(money=input_coin)

        make_coffee(user_input)

        # too much money
        if memu_cost < input_coin:
            print(f'Here is ${round(input_coin - memu_cost, 2)} dollars in change.')
    # money not enough
    else:
        print("Sorry that's not enough money. Money refunded.")
        continue

