# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('blue')
#
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column(fieldname='Pokemon Name', column=['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column(fieldname='Type', column=['Electric', 'Water', 'Fire'])
#
# print(table)

from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


money_machine.report()
