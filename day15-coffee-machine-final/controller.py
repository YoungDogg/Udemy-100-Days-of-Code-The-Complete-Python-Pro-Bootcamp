import os
from main import MENU, resources


def clear():
    os.system('clear')


def check_resources(resources, order):
    # get menu and current resource
    r_water = resources["water"] if resources["water"] else 0
    r_milk = resources["milk"] if resources["milk"] else 0
    r_coffee = resources["coffee"] if resources["coffee"] else 0
    ingredients = MENU[order]["ingredients"] if MENU[order]["ingredients"] else None
    o_water = ingredients["water"] if ingredients["water"] else 0
    o_milk = ingredients["milk"] if ingredients["milk"] else 0
    o_coffee = ingredients["coffee"] if ingredients["coffee"] else 0

    has_resource = True

    # compare each
    if r_water < o_water != 0:
        has_resource = False
        print(f"Sorry there is not enough water.")
    if r_milk < o_milk != 0:
        has_resource = False
        print(f"Sorry there is not enough milk.")
    if r_coffee < o_coffee != 0:
        has_resource = False
        print(f"Sorry there is not enough coffee.")

    if not has_resource:
        return False

    return True


def insert_coin():
    coin_sum = 0
    input_quaters = int(input("input quaters: ")) * .25
    input_dimes = int(input("input dimes: ")) * .1
    input_nickles = int(input("input nickles: ")) * .05
    input_pennies = int(input("input pennies: ")) * .01
    coin_sum = input_quaters+input_dimes+input_nickles+input_pennies

    return coin_sum

def report(money: int = 0):
    print(f'''
            current resource values
            Water: {resources["water"]}
            Milk: {resources["milk"]}
            Coffee: {resources["coffee"]}
            Money: {money}
    ''')

def make_coffee():
    ingredients = MENU[order]["ingredients"] if MENU[order]["ingredients"] else None
    resources["water"] -= ingredients["water"]
    print("Here is your {latte}. Enjoy!")