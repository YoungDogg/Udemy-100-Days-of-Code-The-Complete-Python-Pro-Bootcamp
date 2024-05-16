from controller import clear, check_resources, insert_coin

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

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
is_machine_working = True
money = 0
while is_machine_working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        clear()
        is_machine_working = False

    # TODO: 3. Print report.
    if user_input == "report":
        print(f'''
        current resource values
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: {money}
''')

    # TODO: 4. Check resources sufficient?
    is_resourceful = check_resources(resources, user_input)

    # TODO: 5. Process coins.
    if is_resourceful:
        input_coin = coin_sum()

    # TODO: 6. Check transaction successful?
    if MENU[user_input]["cost"] <= input_coin:
        print("something")
    else:
        print("Sorry that's not enough money. Money refunded.")

    # money not enough
    # enough money
    # too much money

# TODO: 7. Make Coffee.
print("Here is your {latte}. Enjoy!")
