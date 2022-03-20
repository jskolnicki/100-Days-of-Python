import pandas
import os

os.chdir(os.path.dirname(__file__))

df = pandas.read_csv("squirrels.csv")

colors= ['Gray', 'Cinnamon', 'Black']

number_of_squirrels = []

for color in colors:
    number_of_squirrels.append(len(df['Primary Fur Color'] == color))

my_dict = {'Fur Color': colors, 'Squirrels': number_of_squirrels}

csv = pandas.DataFrame(my_dict)

csv.to_csv("csv_by_color.csv.")