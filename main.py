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


def print_report():
    for x in resources:
        print(x + ": " + str(resources[x]))


def check_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for x in drink_ingredients:
        if resources[x] < drink_ingredients[x]:
            print("Sorry there is not enough " + x)
            return False
    return True


def process_coins():
    total = 0
    total += float(input("Quarters: ")) * 0.25
    total += float(input("Dimes: ")) * 0.10
    total += float(input("Nickles: ")) * 0.05
    total += float(input("Pennies: ")) * 0.01
    return total


def check_transaction_successful(drink_price, money_used):
    if money_used < drink_price:
        print("Sorry that's not enough money")
        return False
    else:
        if money_used - drink_price > 0:
            print("Change: "+str(money_used - drink_price))
        return True


def make_coffee(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for x in drink_ingredients:
        resources[x] -= drink_ingredients[x]
    print(resources)


def main():
    # TODO: What would you like?
    loop = True
    while loop:
        choice = input("What would you like?(espresso/latte/cappuccino): ")
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        else:
            if choice in MENU:
                print(choice)
                if check_resources(choice):
                    money = process_coins()
                    if check_transaction_successful(MENU[choice]["cost"], money):
                        make_coffee(choice)




main()
