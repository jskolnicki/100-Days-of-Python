##################### Extra Hard Starting Project ######################

from email import message
from re import template
import pandas as pd
import os
import datetime
import random
import smtplib
from csv import reader

os.chdir(os.path.dirname(__file__))

my_email = "jareds.automated.email@gmail.com"
password = "abcdefg123()"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

df = pd.read_csv("birthdays.csv")


today_string = datetime.date.today().strftime('%m-%d')

with open('birthdays.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            birthday = f'{row[4].zfill(2)}-{row[5].zfill(2)}'

            if birthday == today_string:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv         
                number_of_letter_options = 0
                for letter in os.listdir('letter_templates'):
                    if row[1] in letter:
                        number_of_letter_options += 1
                with open(f'C:/Users/jared/GitHub/continued-ed/100-Days-of-Python/day-32-email/letter_templates/{row[1]}_{random.randint(1,number_of_letter_options)}.txt') as file:
                    message = file.readlines()
                    email_message = ""
                    for line in message:
                        email_message = email_message + line
                    email_message = email_message.replace("[NAME]",row[0])

                    
# 4. Send the letter generated in step 3 to that person's email address.
                    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls()
                        connection.login(user=my_email, password=password)

                        connection.sendmail(from_addr=my_email,
                                            to_addrs=row[2],
                                            msg= f'Subject:Happy Birthday!\n\n{email_message}')