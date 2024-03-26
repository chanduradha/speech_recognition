import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import pywhatkit
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=20)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception as e:
            print("Say that again please...")
            return "none"
        return query.lower()

def wish():
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour <= 12:
            speak("good morning")
            speak("i am jarvis sir.please tell me how can i help you")
        elif hour > 12 and hour < 18:
            speak("good afternoon")
            speak("i am jarvis sir.please tell me how can i help you")
        else:
            speak("good evening")
            speak("i am jarvis sir.please tell me how can i help you")


if __name__ == "__main__":
    wish()
    #while True:
    if 1:

        query = Takecommand().lower()
        # logic building for task

        if "open notepad" in query:
            npath = "C:\\Program Files\\Notepad++\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\SUPRIYA K\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = Takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+917259250836", "this is testing protocol", 2.45)

        elif "play songs on youtube" in query:
            pywhatkit.playonyt("https://www.youtube.com/watch?v=8iCcyOekVpc&pp=ygUZc2FsdXRoaWxsYXZlIGthbm5hZGEgc29uZw%3D%3D")
