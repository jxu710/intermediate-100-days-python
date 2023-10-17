from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMaker = CoffeeMaker()
menu = Menu()
the_money_machine = MoneyMachine()



is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeeMaker.report()
        the_money_machine.report()
    else:
        # drink is the MenuItem object
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            cost = drink.cost
            if the_money_machine.make_payment(cost):
                coffeeMaker.make_coffee(drink)


