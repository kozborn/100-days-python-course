logo = """
_________         _____  _____                _____          __                 
\_   ___ \  _____/ ____\/ ____\____   ____   /     \ _____  |  | __ ___________ 
/    \  \/ /  _ \   __\/   __\/ __ \_/ __ \ /  \ /  \ __  \ |  |/ // __ \_  __ 
\     \___(  <_> )  |   |  | \  ___/\  ___//    Y    \/ __ \|    <\  ___/|  | \/
 \______  /\____/|__|   |__|  \___  >\___  >____|__  (____  /__|_  \ ___  >__|   
        \/                        \/     \/        \/     \/     \/    \/ 
"""

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
    "money": 0
}

def format_money_value(money):
    return str(round(money, 2))

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {format_money_value(resources['money'])}$")

def insert_coins(coin_type):
    return int(input(f"How many {coin_type}?: "))

def check_resource(ingredients, resource):
    if resources[resource] < ingredients[resource]:
        print(f"Sorry, there is not enough {resource}!")
        return False
    return True

def check_resources(coffee_type):
    ingredients = coffee_type['ingredients']
    for key in ingredients:
        if not check_resource(ingredients, key):
            return False
    return True

machine_is_working = True
print(logo)

def check_cost_and_money(cost, money):
    return money >= cost

def update_resources(coffee_type):
    resources["money"] += coffee_type['cost']
    ingredients = coffee_type['ingredients']
    for key in ingredients:
        resources[key] -= ingredients[key]

while machine_is_working:
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0
    total_moneys = 0
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        print_report()
    elif user_choice == "off":
        machine_is_working = False
    elif user_choice not in MENU:
        print(f"Sorry, there is no such option!")
    elif not check_resources(MENU[user_choice]):
        print_report()
        machine_is_working = False
    else:
        coffee = MENU[user_choice]
        print("Please insert coins")
        pennies = insert_coins('pennies')
        nickles = insert_coins('nickels')
        dimes = insert_coins('dimes')
        quarters = insert_coins('quarters')

        total_moneys = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
        if not check_cost_and_money(coffee["cost"], total_moneys):
            print(f"Sorry that's not enough money. Money refunded.({format_money_value(total_moneys)}$)")
        else:
            update_resources(coffee)
            if total_moneys > coffee["cost"]:
                print(f"Here's your change: {format_money_value(total_moneys - coffee['cost'])}$, and hot coffee ☕, enjoy")
            else:
                print("Here's your coffee ☕, enjoy")
