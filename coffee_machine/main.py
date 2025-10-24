import machine_info
import copy

current_resources = copy.deepcopy(machine_info.resources)

def order_coffee():
    selected_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selected_drink=='report':
        print(f"Water : {current_resources['water']}ml")
        print(f"Milk : {current_resources['milk']}ml")
        print(f"Coffee : {current_resources['coffee']}gm")
    elif selected_drink=='espresso':
        print("Insert coins")
        take_coins(selected_drink)
    elif selected_drink=='latte':
        print("Insert coins")
        take_coins(selected_drink)
    elif selected_drink=='cappuccino':
        print("Insert coins")
        take_coins(selected_drink)
    elif selected_drink=='off':
        print("Shutting Down")
        return 0
    else:
        print("Order something from the Menu")

def take_coins(drink):
    while True: 
        try:
            drink_cost = machine_info.MENU[drink]['cost']
            quarters = int(input("Insert quarters: "))
            dimes = int(input("Insert dimes: "))
            nickles = int(input("Insert nickles: "))
            pennies = int(input("Insert pennies: "))
            break
        except ValueError:
            print("Please Enter an Integer Value")

    inserted_amt = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    change = 0
    if inserted_amt >= drink_cost:
        change = inserted_amt-drink_cost
        print(f"Here's your change ${round(change,2)}")
        make_coffee(drink)
        print(f"Here is your {drink}. Enjoy!")
    else:
        print(f"Money Refunded, Please Enter sufficient coins, your {drink} is worth ${drink_cost}")
        take_coins(drink)
        

def make_coffee(drink):
    required_ing = machine_info.MENU[drink]['ingredients']
    for ingredient in required_ing:
        if current_resources[ingredient]>=required_ing[ingredient]:
            current_resources[ingredient] -= required_ing[ingredient]
            print(f"{machine_info.sounds[ingredient]}")
        else:
            print(f"Sorry, we've run out of {ingredient}")



order='y'
while order=='y':
    status = order_coffee()
    if status==0:
        print("Turned off for maintenance, Try again later")
        order='n'
        continue
    order=input("Do you want to order something else? y or n: ")