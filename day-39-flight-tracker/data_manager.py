import os
import requests
import pandas as pd

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    GOOGLE_SHEET_NAME = 'Flights'
    APP_ID = os.environ["PERSONAL_SHEETY_APP_ID"]
    APP_KEY = os.environ["PERSONAL_SHEETY_API_KEY"]
    SHEETY_BEARER_TOKEN = os.environ["PERSONAL_SHEETY_BEARER_TOKEN"]

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
    }

    bearer_headers = {'Authorization': SHEETY_BEARER_TOKEN}

    sheet_endpoint = 'https://api.sheety.co/2e8654f86ce23eb2d2ddf106a5a2b545/flightTracker/flights'


    sheet_response = requests.get(sheet_endpoint, headers=bearer_headers).json()
    pd.DataFrame(sheet_response['flights'])