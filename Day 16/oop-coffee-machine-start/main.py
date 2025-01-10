from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

logo = """
_________         _____  _____                _____          __                 
\_   ___ \  _____/ ____\/ ____\____   ____   /     \ _____  |  | __ ___________ 
/    \  \/ /  _ \   __ \   __\/ __ \_/ __ \ /  \ /   \__  \ |  |/ // __ \_  __ |
\     \___(  <_> )  |   |  | \  ___/\  ___//    Y    \/ __ \|    <\  ___/|  | \/
 \______  /\____/|__|   |__|  \___  >\___  >____|__  (____  /__|_  \___  >__|   
        \/                        \/     \/        \/     \/     \/    \/       """

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
print(logo)
machine_is_on = True
while machine_is_on:
    user_choice = input(f"What would you like? {menu.get_items()}").lower()
    if user_choice == "off":
        machine_is_on = False

    elif user_choice == "report":
        coffee_maker.report()
    elif user_choice == 'profit':
        money_machine.report()

    elif user_choice not in menu.get_items().split('/'):
        print("Sorry, I didn't understand that.")

    elif coffee_maker.is_resource_sufficient(menu.find_drink(user_choice)):
        user_drink = menu.find_drink(user_choice)
        if money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)











