# dictionary_comprehension = {new_key:new_value for item in list}
import pandas as pd
import random

names = ['Jared','David','Aaron','Mike','John','Terry']

my_dict = {name: random.randint(35,100) for name in names}

passed_students = {name: my_dict[name] for name in my_dict if my_dict[name] > 60}



my_df = pd.DataFrame(my_dict, index = [0])

print(passed_students)


test_dict = {'jared':{'hometown':'Pittsburgh'}, 'john':[11,44,11]}

for i in test_dict.items():
    print(i)


# # Exercises
print("\n--- PROBLEM 1---\n")
# You are going to use Dictionary Comprehension to create a dictionary called `result` that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

problem1_dict = {word: len(word) for word in sentence.strip('?').split(" ")}

print(problem1_dict)


print("\n--- PROBLEM 2---\n")

# You are going to use Dictionary Comprehension to create a dictionary called `weather_f`
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: round(num*(9/5) + 32, 1) for (key,num) in weather_c.items()}

print(weather_f)


for (index, row) in my_df.iterrows():
    print(index,row)