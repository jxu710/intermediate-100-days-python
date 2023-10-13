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



# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

order = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
if order == "off":
    exit()

#TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.

if order.lower() == "report":
    for k,v in resources.items():
        print(f"{k}: {v}ml")

# todo 4. Check resources sufficient?
#  a. When the user chooses a drink, the program should check if there are enough
#  resources to make that drink.
#  b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#  not continue to make the drink but print: “Sorry there is not enough water.”
#  c. The same should happen if another resource is depleted, e.g. milk or coffee.

def check_sufficient(order):
    for item in order["ingredients"]:
        print(order["ingredients"][item])


check_sufficient(MENU[order])