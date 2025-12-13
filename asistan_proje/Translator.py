from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans  # pip install googletrans
from gtts import gTTS
import pyttsx3
import speech_recognition
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

from main import language_mode

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        if language_mode == 'tr':
            print("Dinliyorum.....")
        else:
            print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        if language_mode == 'tr':
            print("Anlaşıldı..")
            lang_code = 'tr-TR'
        else:
            print("Understanding..")
            lang_code = 'en-in'
        query = r.recognize_google(audio, language=lang_code)
        print(f"You Said: {query}\n")
    except Exception as e:
        if language_mode == 'tr':
            print("Tekrar eder misin?")
        else:
            print("Say that again")
        return "None"
    return query

def translategl(query):
    if language_mode == 'tr':
        speak("Tabii efendim")
    else:
        speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    if language_mode == 'tr':
        speak("Lütfen çevirmek istediğiniz dili seçin")
    else:
        speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    text_to_translate = translator.translate(query, src="auto", dest=b)
    text = text_to_translate.text
    try:
        speakgl = gTTS(text=text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        if language_mode == 'tr':
            print("Çeviri yapılamıyor")
        else:
            print("Unable to translate")
