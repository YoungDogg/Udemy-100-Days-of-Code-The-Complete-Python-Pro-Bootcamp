import os
from main import MENU


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

    # compare each
    if r_water < o_water != 0:
        print(f"Sorry there is not enough water.")
        return False
    if r_milk < o_milk != 0:
        print(f"Sorry there is not enough milk.")
        return False
    if r_coffee < o_coffee != 0:
        print(f"Sorry there is not enough coffee.")
        return False

    return True


def insert_coin():
    coin_sum = 0
    input_quaters = int(input("input quaters: ")) * .25
    input_dimes = int(input("input dimes: ")) * .1
    input_nickles = int(input("input nickles: ")) * .05
    input_pennies = int(input("input pennies: ")) * .01
    return coin_sum