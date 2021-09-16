
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit as pwt
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'AI' in command:
                command = command.replace('AI', '')
                print(command)
    except:
        pass
    return command


def runAI():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pwt.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('now is ' + time)
    elif 'who is ' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'facebook' in command:
        webbrowser.open('https://www.facebook.com/')  
    elif 'who is product owner'in command:
        talk('there is him git')
        webbrowser.open('https://github.com/Bluxuna')          
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'stop' in command:
        exit()  
    elif 'translate' in command:
        pwt.search('translate')
    else:
        talk('i am searching google it')
        pwt.search(command)


while True:
    runAI()
