import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Dinliyorum.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Anlaşıldı..")
        query  = r.recognize_google(audio,language='tr-TR')
        print(f"Söylediğiniz: {query}\n")
    except Exception as e:
        print("Tekrar eder misin?")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Whatsapp açılıyor")
    # Open WhatsApp desktop application - update the path if needed
    whatsapp_path = r"C:\\Users\\Hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
    try:
        os.startfile(whatsapp_path)
    except Exception as e:
        speak("Whatsapp uygulaması açılamadı, lütfen dosya yolunu kontrol edin.")
