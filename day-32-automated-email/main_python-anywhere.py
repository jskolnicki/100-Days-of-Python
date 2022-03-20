#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas as pd
import random
import smtplib
import os

MY_EMAIL = "jareds.automated.email@gmail.com"
MY_PASSWORD = "abcdefg123()"


data = pd.read_csv(r"C:\Users\jared\GitHub\continued-ed\100-Days-of-Python\day-32-email\birthdays.csv")


today_string = datetime.today().strftime('%m-%d')


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


for (index, row) in data.iterrows():

    birthday = f'{str(row.month).zfill(2)}-{str(row.day).zfill(2)}'
    if birthday == today_string:
        number_of_letter_options = 0
        for letter in os.listdir('day-32-email/letter_templates'):
            if row[1] in letter:
                number_of_letter_options += 1
        file_path = f"day-32-email/letter_templates/{row.relationship}_{random.randint(1,number_of_letter_options)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", str(row.person))

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row.email,
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )