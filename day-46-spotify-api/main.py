from bs4 import BeautifulSoup
import re
import requests

def get_date_input():
    while True:
        date_input = input("Enter the date in the format 'YYYY-DD-MM': ")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_input):
            return date_input
        else:
            print("Invalid format. Please try again.")

date = get_date_input()

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)