# Coffee machine
from Coffee_assets import MENU, resources

flavour = input("What would you like? (espresso/latte/cappuccino): ")
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def resources_check(flavour,req_water,req_coffee,req_milk):
    if flavour == "espresso" or "latte" or "cappuccino": 
        if req_water <= water:
            if req_coffee < coffee:
                if req_milk < milk:
                    return True
                else:
                    print("Not sufficient milk")
            else:
                print("Not sufficient coffee")
        else:
            print("Not sufficient water")
            
def processing_coins(req_money):
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    
    money = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25 
    if money > req_money:
        return money - req_money
    elif money < req_money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        return   

def coffee_machine(flavour, water, coffee, milk):
    if flavour == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
    else:
        req_coffee = MENU[f"{flavour}"]["ingredients"]["coffee"]
        req_water = MENU[f"{flavour}"]["ingredients"]["water"]
        req_milk = MENU[f"{flavour}"]["ingredients"]["milk"]
        req_money = MENU[f"{flavour}"]["cost"] 
        # resources_check(flavour,req_water,req_coffee,req_milk)   
        if resources_check(flavour,req_water,req_coffee,req_milk) == True:
            change = processing_coins(req_money)
            print(f"Here is ${change} in change")
            print(f"Here is your {flavour}. Enjoy!")
            water -= req_water
            coffee -= req_coffee
            milk -= req_coffee
            resources.update({f"water":{water}, "milk":{milk}, "coffee":{coffee}})

coffee_machine(flavour, water, coffee, milk)     



    


            
            
            

