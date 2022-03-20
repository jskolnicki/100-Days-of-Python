import pandas
import os
import csv

os.chdir(os.path.dirname(__file__))


# DON'T ACTUALLY DO IT THIS WAY. PANDAS IS WAY BETTER (obviously)

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for line in data:
#         if line[1] != 'temp':
#             temperature.append(int(line[1]))

df = pandas.read_csv("weather_data.csv")

print(df[df['temp'] == df['temp'].max()])

print(df[df.day == 'Monday'])

temp_list = df.temp.to_list()

fahrenheit_list = []
for temp in temp_list:
    temp = temp * (9/5) + 32
    fahrenheit_list.append(temp)

df.temp = fahrenheit_list

print(df)