import pandas
import os

os.chdir(os.path.dirname(__file__))

squirrels = pandas.read_csv("squirrels.csv")

for (test, row) in squirrels.head(10).iterrows():
    if row.Date == 10182018:
        print(row)