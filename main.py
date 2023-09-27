from data import MENU, resources


class ResourceCheckResult:
    def __init__(self, resources_available, message):
        self.resources_available = resources_available
        self.message = message


def check_resources(required_ingredients):
    result = ResourceCheckResult(True, "")
    for key in required_ingredients:
        if resources[key] < required_ingredients[key]:
            result.resources_available = False
            result.message = result.message + (f"Not enough {key}: required amount {required_ingredients[key]} and "
                                               f"available amount {resources[key]}: ")
    return result


def insert_coins():
    coins = {
        "quarters": {"value": 0.25, "quantity": 0},
        "dimes": {"value": 0.10, "quantity": 0},
        "nickles": {"value": 0.05, "quantity": 0},
        "pennies": {"value": 0.01, "quantity": 0},
    }
    for key in coins:
        quantity = int(input(f"how many {key} "))
        coins[key]["quantity"] = quantity
    return coins


def calculate_total(coins):
    total = 0.0
    for key in coins:
        total += coins[key]["value"] * coins[key]["quantity"]
    return total


def complete_transaction(required_ingredients, cost):
    for key in required_ingredients:
        resources[key] -= required_ingredients[key]
    resources["money"] += cost


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    ingredients = MENU[choice]["ingredients"]
    result = check_resources(ingredients)
    if result.resources_available:
        coins = insert_coins()
        total_inserted = calculate_total(coins)
        if total_inserted < MENU[choice]["cost"]:
            print(f"message sorry not enough money, refunded {total_inserted} ")
        else:
            change = total_inserted - MENU[choice]["cost"]
            complete_transaction(ingredients,MENU[choice]["cost"])
            print(f"Enjoy your {choice}")
            if change > 0:
                print(f"Here is your change {change}")


