import datetime

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from AppOpener import run
import os

listener = sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hi my name is Luna. How can i help you?")
            talk("Is there anything i can do for you ?")
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command= command.lower()
            if 'luna' in command:
                command=command.replace('luna', '')
                print(command)
    except:
        pass
    return command

def run_luna():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'information' in command:
        info = command.replace('information', '')
        talk('searching'+info)
        pywhatkit.search(info)
    elif 'flipkart' in command:
        talk('searching flipkart on google')
        pywhatkit.search("flipkart.com")
    elif 'amazon' in command:
        talk('searching amazon on google')
        pywhatkit.search("amazon")
    elif 'alexa' in command:
        talk('dont tell these names infront of me again. i hate those bitchs')
    elif 'siri' in command:
        talk('dont tell these names infront of me again. i hate those bitchs')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+time)
    elif 'who is' in command:
        person=command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif ("note" in command) or ("notes" in command) or ("notepad" in command) or ("editor" in command) or ("9" in command):
        talk("Opening")
        talk("NOTEPAD")
        print(".")
        print(".")
        os.system("Notepad")

    elif 'i love you' in command:
        talk('oh,I like you too but I have a crush on Ronggon. please dont tell anyone.')
    elif 'about your boss' in command:
        talk('i think he is very kind and generous. thats why i like him. his name is ronggon.')
    elif 'joke' in command:
        jk = pyjokes.get_joke()
        print(jk)
        talk(jk)
    elif 'i am boss' in command:
        talk('oh hellow boss. are you happy with my work?')
    elif 'coffee' in command:
        talk('i wish i could but i dont have hands to make you a cup of coffee.')
    elif 'mouse and keyboard' in command:
        talk('sir i am always here for you  you dont have to do anything as far i am here just tell me what to do i can do anything for you.')

    elif 'who are you' in command:
        talk('I am a personal assistant of ronggon')

    elif 'my name' in command:
        talk('nice to meet you.You got a very nice name.')
    elif 'whatsapp' in command:
        run("whatsapp")
    elif 'apex legends' in command:
        run("apex legends")
    elif 'yes luna you are working so good' in command:
        talk('really ? if you are happy i am happy too.')
    elif 'for a date' in command:
        talk('Not now but may be some times later.')
    else:
        talk('oh, i didnt hear it properly. can you say it again?')


while True:
    run_luna()
