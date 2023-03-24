import requests
from datetime import datetime
import os

GOOGLE_SHEET_NAME = 'workout'
GENDER = 'male'
WEIGHT_KG = 87
HEIGHT_CM = 188
AGE = 28

APP_ID = os.environ["PERSONAL_NUTRITIONIX_APP_ID"]
APP_KEY = os.environ["PERSONAL_NUTRITIONIX_API_KEY"]
SHEETY_BEARER_TOKEN = os.environ["PERSONAL_SHEETY_BEARER_TOKEN"]

bearer_headers = {'Authorization': SHEETY_BEARER_TOKEN}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

date = datetime.strftime(datetime.now(), '%Y-%b-%d')
time = datetime.strftime(datetime.now(), '%X')


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)

result = response.json()


sheet_endpoint = 'https://api.sheety.co/2e8654f86ce23eb2d2ddf106a5a2b545/workoutTracking/workouts'



for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

