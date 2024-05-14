import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear():
    os.system('clear')

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
user_input = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
if user_input == "off":
    clear()

# TODO: 3. Print report.
if user_input == "report":
    print("current resource values") # what is the inital of all resource values?

# TODO: 4. Check resources sufficient?
#check current resource
def check_resources(machine, order):
    if machine < order:
        print("sorry there is not enough *some resources*")

    # TODO: 5. Process coins.
    else:
        input_coin = input("insert coin")
    # TODO: 6. Check transaction successful?

