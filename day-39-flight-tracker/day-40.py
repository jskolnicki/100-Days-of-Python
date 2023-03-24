import os
import requests


APP_ID = os.environ["PERSONAL_SHEETY_APP_ID"]
APP_KEY = os.environ["PERSONAL_SHEETY_API_KEY"]
SHEETY_BEARER_TOKEN = os.environ["PERSONAL_SHEETY_BEARER_TOKEN"]
GOOGLE_SHEET_NAME = 'company'


bearer_headers = {'Authorization': SHEETY_BEARER_TOKEN}
sheet_endpoint = 'https://api.sheety.co/2e8654f86ce23eb2d2ddf106a5a2b545/flightTracker/company'

first_name = input('What is your first name?')
last_name = input('What is your last name?')
email = input('What is your email?')

sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "firstName": first_name, #keys must be camelcase
            "lastName": last_name,
            "email": email
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)