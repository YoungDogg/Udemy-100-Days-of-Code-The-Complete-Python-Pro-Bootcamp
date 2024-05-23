from config import MENU, resources

def check_resources(resources, drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    is_resourceful = True
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_resourceful = False
    return is_resourceful


def insert_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def report(money=0):
    print(f"""
current resource values
Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: {money}
""")

def make_coffee(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")