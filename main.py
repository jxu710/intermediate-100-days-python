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

choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
if choice == "off":
    exit()

#TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.

if choice.lower() == "report":
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
        # print(order["ingredients"][item])
        if resources[item] < order["ingredients"][item]:
            print(f"Sorry there is not enough {resources[item]}")
            return False
        else:
            return True


check_sufficient(MENU[choice])

# TODO 5. Process coins.
#  a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#  b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#  c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#  pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

if check_sufficient(MENU[choice]):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?:  "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.10
    nickles_value = nickles * 0.05
    pennies_value = pennies * 0.01

    total_value_inserted = quarters_value + dimes_value + nickles_value+pennies_value

    if total_value_inserted < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total_value_inserted >= MENU[choice]["cost"]:
        change = round(total_value_inserted - MENU[choice]["cost"], 2)
        print(f"Here is ${change} in change.\nHere is your {choice} ☕️. Enjoy!")