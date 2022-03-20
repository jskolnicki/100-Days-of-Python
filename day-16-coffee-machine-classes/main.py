# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()

# timmy.color("DeepPink")

# timmy.shape("turtle")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(130)


# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",['Pikachu','Charizard','Squirtle','Bulbasaur'], align='l')
table.add_column("Type",['Electric','Fire','Water','Grass'], align='r')

print(table)