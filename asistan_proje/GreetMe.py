import pyttsx3
import datetime
from main import language_mode

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if language_mode == 'tr':
        if hour >= 0 and hour <= 12:
            speak("Günaydın efendim")
        elif hour > 12 and hour <= 18:
            speak("Tünaydın efendim")
        else:
            speak("İyi akşamlar efendim")
        speak("Size nasıl yardımcı olabilirim?")
    else:
        if hour >= 0 and hour <= 12:
            speak("Good Morning, sir")
        elif hour > 12 and hour <= 18:
            speak("Good Afternoon, sir")
        else:
            speak("Good Evening, sir")
        speak("Please tell me, How can I help you ?")
