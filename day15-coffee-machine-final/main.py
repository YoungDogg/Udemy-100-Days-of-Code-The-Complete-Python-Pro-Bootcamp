from controller import clear, check_resources, insert_coin, report

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

while is_machine_working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        clear()
        is_machine_working = False

    # TODO: 3. Print report.
    if user_input == "report":
        report()

    # TODO: 4. Check resources sufficient?
    is_resourceful = check_resources(resources, user_input)
    memu_cost: int = MENU[user_input]["cost"]
    if not is_resourceful:
        print("please pick other drink")
        continue

    # TODO: 5. Process coins.
    if is_resourceful:
        input_coin = insert_coin()

    # TODO: 6. Check transaction successful?
    # enough money
    if memu_cost <= input_coin:
        report(money=input_coin)
        # TODO: 7. Make Coffee.
        make_coffee(user_input)

        # too much money
        if memu_cost < input_coin:
            print(f'Here is ${round(input_coin - memu_cost, 2)} dollars in change.')
    # money not enough
    else:
        print("Sorry that's not enough money. Money refunded.")
        continue



