MENU = {
    "espresso": {
        "ingredients": {
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte": {
        "ingredients": {
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

profit = 0

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def isResourceSufficient(orderIngredients):
    """
    Check if it's possible to make the order
    :param orderIngredients:
    :return:
    True when order can be made, False if ingredients are insufficient
    """
    for item in orderIngredients:
        if orderIngredients[item] >= resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def processCoins():
    """
    Calculate the total
    :return:
    total calculated from coins inserted
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def isTransactionSuccessful(moneyReceived, drinkCost):
    """
    Check if the payment accepted or not
    :param moneyReceived:
    :param drinkCost:
    :return:
    True when the payment is accepted, False if money is insufficient.
    """
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost)
        print(f"Here is ${change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def makeCoffee(drinkName, orderIngredients):
    """
    Deduct the required ingredients from the resources
    :param drinkName:
    :param orderIngredients:
    :return:
    """
    for item in orderIngredients:
        resource[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} 🍵")

isOn = True

while isOn:
    choice = input("What would you like? (espresso, latte, cappuccino):\n")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])