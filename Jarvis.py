import pyttsx3
import pywin32_system32
import datetime
import pytz
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import random
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def time():
    time = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I : %M")
    speak("The current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)   
    month = int(datetime.datetime.now().month) 
    date = int(datetime.datetime.now().day) 
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def greet():
    hour = datetime.datetime.now().hour  
    if hour in range(6, 12):
        speak("Good morning")
    elif hour in range(12, 18):
        speak("Good afternoon")
    elif hour in range(18, 25):
        speak("Good evening")
    else:
        speak("Good night")
    time()
    date()           
    speak("How can I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ()
        print ("Listening...")  
        r.pause_threshold = 1
        audio = r.listen(source)   
    try:
        print ("Recognizing...")
        query = r.recognize_google(audio, language = "en - in")
        print (query)
    except Exception as e:
        print (e)
        speak("Pardon me")
        return "None"    
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("", "")
    server.sendmail("", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sumit\\Desktop\\Bhavesh\\Python\\Jarvis\\Screenshots.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())      

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()  

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "") 
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif "email" in query:
             try:
                 speak("What should I write in it ?")
                 content = takeCommand()
                 to = ""
                 sendEmail(to, content)
                 speak("Email sent")  
             except Exception as e:
                 print (e)
                 speak("Unable to send email")

        elif "what all can you do" in query or "what can you do" in query:
            speak("I can")
            speak("Wikipedia search")
            speak("Send emails")
            speak("Chrome search")
            speak("Play songs")
            speak("Tell jokes") 
            speak("And many more") 

        elif "what is your name" in query:
            speak("My name is JARVIS")

        elif "what is my name" in query:
            speak("Your name is BHAVESH")

        elif "search" in query:
            speak("What should I search ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "when were you born" in query:
            speak("I was born on 25th of June 2020")     

        elif "log out" in query:
            os.system("shutdown -1") 

        elif "shut down" in query:
            os.system("shutdown /s /t 1") 

        elif "restart" in query:
            os.system("shutdown /r /t 1") 

        elif "play songs" in query:
            song1 = "https://www.youtube.com/watch?v=qFkNATtc3mc"
            song2 = "https://www.youtube.com/watch?v=T8qZ-t6c49w"
            song3 = "https://www.youtube.com/watch?v=IDSMj9wM9Os"
            song4 = "https://www.youtube.com/watch?v=vjOKuvBjkS8" 
            song5 = "https://www.youtube.com/watch?v=qFkNATtc3mc"
            song6 = "https://www.youtube.com/watch?v=OgCVBmIlIro"
            song7 = "https://www.youtube.com/watch?v=6nIcjua7YSo"
            song_dir = [song1, song2, song3, song4, song5, song6, song7]
            song = random.choice(song_dir)
            os.startfile(os.path.join(song))  

        elif "remember" in query:
            speak("What should I remember ?")   
            data = takeCommand()
            speak("You said me to remember" + data)
            remember = open("Data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know" in query or "do you remember" in query:
            remember = open("Data.txt", "r")
            speak("You said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken")

        elif "cpu" in query or "battery" in query:
            cpu()

        elif "joke" in query or "jokes" in query:
            jokes()      

        elif "offline" in query or "exit" in query or "bye" in query or "stop" in query:
            speak("Ok")
            quit() 
