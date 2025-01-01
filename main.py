import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def print_hi(name):
    print(f'Hi, {name}')

while True:
    print("Hello, I am Jarvis A.I.")btw
    s = input("Please enter some text: ")
    speaker.Speak(s)
    if s.lower() == "exit":
        break

if __name__ == '__main__':
    print_hi('Pycharm')