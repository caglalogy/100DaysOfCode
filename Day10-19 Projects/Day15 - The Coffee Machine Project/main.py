import menu

resources = menu.resources
coffees = menu.MENU
current_money = 0.0


# TODO: 5. take data from menu.py
def give_report():
    """
    This function print the report of all resources currently in the machine.
    """

    print(f"""
    Water:  {resources["water"]}ml
    Milk:   {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money:  ${current_money}
     """)


def check_resources(coffee_type):
    """
    This function checks before take money from user if there are enough resources to do the given task.

    :param coffee_type:
    :return:
    """

    water = resources["water"] - coffees[coffee_type]["ingredients"]["water"]
    coffee = resources["coffee"] - coffees[coffee_type]["ingredients"]["coffee"]
    milk = resources["milk"] - coffees[coffee_type]["ingredients"]["milk"]

    if water >= 0 and coffee >= 0 and milk >= 0:
        return 1  # enough resources.
    else:
        print("insufficient resource!")
        return 0  # insufficient resources


def add_resources(res_type, amount):
    """
    This is an admin option, helps of this function, admin can add resources to the machine.

    :param res_type:
    :param amount:
    :return:
    """
    resources[res_type] += amount
    print("Resources are updated.")
    give_report()


def process_coins(coffee_type):
    """
    This function takes money from user and calculate change, update current money in the machine.
    If the money is not enough to pay for drink, makes it refunded.

    :param coffee_type:
    :return:
    """
    print("Please insert coins.")
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    pe = int(input("How many pennies? "))
    total_inserted_coins = (q * 0.25) + (d * 0.1) + (n * 0.05) + (pe * 0.01)

    if total_inserted_coins >= coffees[coffee_type]["cost"]:
        global current_money
        current_money += coffees[coffee_type]["cost"]
        change = total_inserted_coins - coffees[coffee_type]["cost"]
        change = float("{:.2f}".format(change))
        print(f"Here is ${change} in change.")
        return 1
    else:
        print("Sorry that's not enough money. Money refunded.")
        return -1


def give_drink(coffee_type):
    """
    This function gives the drink which is requested by user on the menu. Updates resources.
    :param coffee_type:
    :return:
    """
    if check_resources(coffee_type) == 1:
        resources["water"] -= coffees[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= coffees[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= coffees[coffee_type]["ingredients"]["milk"]

        print(f"Here your {coffee_type}")
    else:
        print("insufficient resource!")


def main():
    """
    User screen to use coffee machine. Follow the instructions.
    :return:
    """
    request = input("What would you like? (espresso/latte/cappuccino): ").strip()
    if request == "off":
        print("System is closed.")
        return

    elif request == "report":
        give_report()
        main()

    elif request == "admin":
        print("System settings:")
        print("1 - Empty money box")
        print("2 - Add resources")
        admin_option = int(input("(1/2): "))
        if admin_option == 1:
            global current_money
            current_money = 0
            print("Money box is emptied.")
            main()
        elif admin_option == 2:
            res = input("What do you want to add resource tank? (water/milk/coffee): ")
            amount = int(input(f"How much do you want to add {res}?"))
            if res in ["water", "milk", "coffee"]:
                add_resources(res, amount)
                main()
            else:
                print("Undefined resource type.")
                main()

    elif request in ["espresso", "latte", "cappuccino"]:
        if check_resources(request) == 1:
            if process_coins(request) == 1:
                give_drink(request)
        main()

    else:
        print("undefined input.")
        main()


main()
