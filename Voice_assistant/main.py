import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import requests
import wolframalpha


## declaring variables
listener = sr.Recognizer()                      #speech recognition
engine = pyttsx3.init()                         #text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):                                 #talk function
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:

        print("Hello,Good Morning")
        talk("Hello,Good Morning")
    elif hour>=12 and hour<18:

        print("Hello,Good Afternoon")
        talk("Hello,Good Afternoon")
    else:

        print("Hello,Good Evening")
        talk("Hello,Good Evening")

def take_command():                                         #Identifies the command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,None,10)         #User's input is taken
            command = listener.recognize_google(voice)      #User's command is recognised by Google api
            command = command.lower()

    except:
        pass
    return command


print('Loading your AI personal assistant')
talk("Loading your AI personal assistant ")
wishMe()
print("How can i help you?")
talk("how can i help you")



def run_alexa():                                                        #Runs all the commands
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        os._exit(0)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)


    elif 'who is' in command:
        person = command.replace('who  is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        x = datetime.date.today()

        talk('todays date is')
        talk(x)
        print('todays date is')
        print(x)

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        os._exit(0)

    elif 'open google' in command:
        talk("Here you go to google\n")
        webbrowser.open("google.com")
        os._exit(0)


    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open github' in command:
        talk("Here you go to github\n")
        webbrowser.open("github.com")
        os._exit(0)

    elif 'open stackoverflow' in command:
        talk("Here you go to stackoverflow\n")
        webbrowser.open("stackoverflow.com")
        os._exit(0)



    elif 'news' in command:
        talk("Here are headlines of today\n")
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
        os._exit(0)



    elif "word" in command:
        talk("Opening Microsoft Word")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
        os._exit(0)


    elif "excel" in command:
        talk("Opening Microsoft Excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
        os._exit(0)

    elif "powerpoint" in command:
        talk("Opening Microsoft Excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
        os._exit(0)

    elif "chrome" in command:
        talk("Google Chrome")
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        os._exit(0)

    elif "goodbye" in command or "bye" in command:
        talk("ok,Bye,I am logging off")
        os._exit(0)

    elif 'maths' in command or "geographical" in command:
        talk('what question do you have')
        question = take_command()
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)


    elif "weather" in command:

        api_key = "8ef61edcf1c576d65d836254e11ea420"

        base_url = "https://api.openweathermap.org/data/2.5/weather?"

        talk("whats the city name")

        city_name = take_command()

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = y["temp"]

            current_humidiy = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]

            talk(" Temperature in kelvin unit is " +

                  str(current_temperature) +

                  "\n humidity in percentage is " +

                  str(current_humidiy) +

                  "\n description  " +

                  str(weather_description))

            print(" Temperature in kelvin unit = " +

                  str(current_temperature) +

                  "\n humidity (in percentage) = " +

                  str(current_humidiy) +

                  "\n description is " +

                  str(weather_description))


        else:

            talk(" City Not Found ")

while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print("Pardon me, please say that again")
        talk("Pardon me, please say that again ")
        command = ""
        print(command)