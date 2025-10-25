from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
coin_machine = MoneyMachine()

def order_and_get():
    selected_drink = input(f"What would you like? {menu.get_items()}   ").lower()
    if selected_drink=='off':
        return
    elif selected_drink=='report':
        coffee_maker.report()
        coin_machine.report()
        return
    else:
        menu.find_drink(selected_drink)
        if(coin_machine.make_payment(menu.find_drink(selected_drink).cost)):
            if(coffee_maker.is_resource_sufficient(menu.find_drink(selected_drink))):
                coffee_maker.make_coffee(menu.find_drink(selected_drink))


start = 'y'
while start == 'y':
    order_and_get()
    start=input("Would you like to order again? y or n ")