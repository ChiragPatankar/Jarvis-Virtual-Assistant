import os
import sys
import cv2
import speech_recognition as sr
import pyttsx3  # Cross-platform TTS engine
import webbrowser
import datetime
import wikipedia
import pyautogui
import pywhatkit as kit
import time
import random
import requests
import pytz
from forex_python.converter import CurrencyRates
import openai

# Initialize OpenAI API key
openai.api_key = ""

# Initialize pyttsx3 engine
engine = pyttsx3.init()


# Function to convert text to speech
def say(text):
    engine.say(text)
    engine.runAndWait()


# Function to greet based on time
def wishme():
    hour = datetime.datetime.now().hour
    if hour < 12:
        say("Good Morning, Boss!")
    elif hour < 18:
        say("Good Afternoon, Boss!")
    else:
        say("Good Evening, Boss!")


# Function to take voice command
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.6
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that. Please repeat.")
        return take_command()
    except sr.RequestError:
        say("Sorry, there was a problem with the speech recognition service.")
        return ""


# Weather fetching function
def get_weather(city):
    api_key = "39847158f3a1381b781c36165b5a289c"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The weather in {city} is {description} with a temperature of {temp}°C"
    else:
        return "I couldn't retrieve the weather information."


# News fetching function
def get_news():
    api_key = "26f3a5d17d9f4c719e3e19fe11f6b487"  # Replace with your API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json()['articles'][:5]  # Get top 5 news
        headlines = [article['title'] for article in articles]
        return "Here are the top headlines:\n" + "\n".join(headlines)
    else:
        return "I couldn't retrieve the news."


# Currency conversion function
def currency_conversion(amount, from_currency, to_currency):
    try:
        c = CurrencyRates()
        result = c.convert(from_currency, to_currency, amount)
        return f"{amount} {from_currency} is equal to {result:.2f} {to_currency}"
    except:
        return "Sorry, I couldn't perform the currency conversion."


# Open a predefined site
def open_site(site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "instagram": "https://www.instagram.com",
        "google": "https://www.google.com",
        "mail": "https://mail.google.com"
    }
    site = sites.get(site_name)

    if site:
        webbrowser.open(site)
        say(f"Opening {site_name}...")
    else:
        say(f"I couldn't find {site_name}.")


# Ask ChatGPT a question
def ask_chatgpt(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            temperature=0.5,
            max_tokens=150,
        )
        answer = response.choices[0].message['content']
        say(answer)
    except Exception as e:
        say("I couldn't get a response from ChatGPT at the moment.")


# Handle user commands
def handle_command(command):
    if "weather" in command:
        city = command.split("in")[-1].strip()
        say(get_weather(city))
    elif "set timer for" in command:
        duration = int(command.split("for")[-1].split()[0])
        time.sleep(duration * 60)
        say("Time's up!")
    elif "news" in command:
        say(get_news())
    elif "convert" in command and "to" in command:
        parts = command.split()
        amount = float(parts[1])
        from_currency = parts[2].upper()
        to_currency = parts[-1].upper()
        say(currency_conversion(amount, from_currency, to_currency))
    elif "open" in command:
        site_name = command.split("open")[-1].strip()
        open_site(site_name)
    elif "search youtube for" in command:
        search_term = command.replace("search youtube for", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
        say(f"Searching YouTube for {search_term}.")
    elif "search google for" in command:
        search_term = command.replace("search google for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        say(f"Searching Google for {search_term}.")
    elif "volume up" in command:
        pyautogui.press("volumeup", presses=6)
    elif "volume down" in command:
        pyautogui.press("volumedown", presses=6)
    elif "mute" in command or "unmute" in command:
        pyautogui.press("volumemute")


    elif "ask chatgpt" in command:
        prompt = command.replace("ask chatgpt", "").strip()
        ask_chatgpt(prompt)
    else:
        say("Sorry, I didn't catch that.")


# Main function
def main():
    wishme()
    while True:
        command = take_command()
        if "bye-bye" in command:
            say("Goodbye Boss! Have a great day!")
            break
        handle_command(command)


if __name__ == '__main__':
    main()
