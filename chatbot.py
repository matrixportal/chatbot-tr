import random
import json
import requests
import datetime
import pytz
import subprocess

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Chatbot"

def run_poem_generator():
    subprocess.run(["python", "şiiryaz.py"], check=True)

print("Hadi sohbet edelim!! (Çıkmak 'quit' yazınt)")

while True:
    sentence = input("Siz: ")
    if sentence == "quit":
        break

    if sentence == "şaşırt beni":
        run_poem_generator()
    else:
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    if tag == "saat":
                        tz_istanbul = pytz.timezone('Europe/Istanbul')
                        now = datetime.datetime.now(tz_istanbul)
                        response = f"{bot_name}: Şu an saat {now.strftime('%H:%M')}"
                    elif tag == "saatlik_hava_raporu":
                        api_key = "2cd340c3bf9f2ed8399dd453167a192b"
                        city = "Izmir"
                        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
                        weather_data = requests.get(url).json()
                        condition = weather_data['weather'][0]['description']
                        temp = weather_data['main']['temp']
                        feels_like = weather_data['main']['feels_like']
                        response = f"{bot_name}: Şu an hava {condition}, sıcaklık {temp} derece, hissedilen sıcaklık {feels_like} derece"
                    elif tag == "günlük_hava_raporu":
                        api_key = "2cd340c3bf9f2ed8399dd453167a192b"
                        city = "Izmir"
                        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
                        weather_data = requests.get(url).json()
                        condition = weather_data['weather'][0]['description']
                        temp = weather_data['main']['temp']
                        feels_like = weather_data['main']['feels_like']
                        humidity = weather_data['main']['humidity']
                        wind_speed = weather_data['wind']['speed']
                        response = f"{bot_name}: {city} şehrinde hava {condition}, sıcaklık {temp} derece, hissedilen sıcaklık {feels_like} derece, nem oranı %{humidity}, rüzgar hızı {wind_speed}km/sa"
                    elif tag == "haftalık_hava_raporu":
                        api_key = "2cd340c3bf9f2ed8399dd453167a192b"
                        city = "Izmir"
                        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
                        weather_data = requests.get(url).json()
                        forecasts = weather_data['list']
                        response = f"{bot_name}: {city} şehrindeki hava durumu tahminleri:\n"
                        for forecast in forecasts:
                            time = datetime.datetime.fromtimestamp(forecast['dt'], tz=pytz.utc).astimezone(pytz.timezone('Europe/Istanbul'))
                            condition = forecast['weather'][0]['description']
                            temp = forecast['main']['temp']
                            response += f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {condition}, sıcaklık {temp} derece\n"
                    else:
                        response = f"{bot_name}: {random.choice(intent['responses'])}"
                    print(response)
        else:
            print(f"{bot_name}: Anlamadım, tekrar söyler misiniz?")
