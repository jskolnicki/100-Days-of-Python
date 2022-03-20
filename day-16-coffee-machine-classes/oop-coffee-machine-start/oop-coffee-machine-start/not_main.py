import coffee_maker
import money_machine
import menu

#Hollywood😎

#set an object vending machine called randy
randy = menu.Menu()

print(randy.get_items())

simon = menu.MenuItem(name='peanut butter',water='water',milk='milk',coffee='coffee',cost= 4)

print(simon)

paula = coffee_maker.CoffeeMaker()

paula.report()

randy.get_items()