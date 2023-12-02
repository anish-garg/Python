# Coffee machine
from Coffee_assets import MENU, resources

is_work_over = False

def resources_check(flavour,req_water,req_coffee,req_milk):
    if flavour == "espresso" or "latte" or "cappuccino": 
        if req_water <= resources["water"]:
            if req_coffee < resources["coffee"]:
                if req_milk < resources["milk"]:
                    return True
                else:
                    print("Not sufficient milk")
            else:
                print("Not sufficient coffee")
        else:
            print("Not sufficient water")
            
def processing_coins(req_money):
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    
    money = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
    if money >= req_money:
        return money - req_money
    elif money < req_money:
        print("Sorry that's not enough money. Money refunded.")
    
while not is_work_over:
    def coffee_machine():
        flavour = input("What would you like? (espresso/latte/cappuccino): ")
        if flavour == "off":
            is_work_over == True
        elif flavour == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}ml')
        else:
            req_coffee = MENU[f"{flavour}"]["ingredients"]["coffee"]
            req_water = MENU[f"{flavour}"]["ingredients"]["water"]
            req_milk = MENU[f"{flavour}"]["ingredients"]["milk"]
            req_money = MENU[f"{flavour}"]["cost"] 
            # resources_check(flavour,req_water,req_coffee,req_milk)   
            if resources_check(flavour,req_water,req_coffee,req_milk) == True:
                change = round(processing_coins(req_money), 2)
                print(f"Here is ${change} in change")
                print(f"Here is your {flavour} ☕️. Enjoy!")
                resources["water"] -= req_water
                resources["coffee"] -= req_coffee
                resources["milk"] -= req_coffee

    coffee_machine()