import speech_recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from wikipedia import PageError

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_name():
    print("what would you like to call me?")
    talk("what would you like to call me")
    take_name.name = take_task()
    print("hi i am", take_name.name)
    intro = "hi i am " + take_name.name
    talk(intro)
    talk("what can i do for you")


def take_task():
    try:
        try:
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    listener.adjust_for_ambient_noise(source)
                    while True:
                        voice = listener.listen(source)
                        task = listener.recognize_google(voice)
                    task = task.lower()
            except UnboundLocalError:
                print("unbound")
        except speech_recognition.UnknownValueError:
            print(" ")
    except UnboundLocalError:
        print("unbound")
    return task

def is_valid(text):
    if take_name.name in text:
        return True
    else:
        talk('try a valid command')
        print('the command is not valid')
        run_bot()


def run_bot():
    command = take_task()
    if is_valid(command):
        command = command.replace(take_name.name, '')
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(time)
        elif 'who is' in command:
            try:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except PageError:
                talk("sorry there are no results ")
        elif 'what' in command:
            try:
                person = command
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except PageError:
                talk("sorry there are no results ")
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            engine.setProperty("rate", 130)
            talk(pyjokes.get_joke())
            engine.setProperty("rate", 160)
        else:
            talk('invalid command')


def take_next():
    talk('do you want anything else')
    print('do you want anything else')
    repeat = take_task()
    print(repeat)
    if 'yes' in repeat:
        run_bot()
        take_next()
    elif 'no' in repeat:
        talk("thank you")
        print("thank you")
        exit()
    else:
        talk('Please say the command again.')
        take_task()
        run_bot()
        take_next()


take_name()


run_bot()


take_next()


