import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Anlaşıldı..")
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Söylediğiniz: {query}\n")
    except Exception as e:
        print("Tekrar eder misin?")
        return "None"
    return query

def game_play():
    speak("Taş, Kağıt, Makas oynayalım!")
    print("OYUNA BAŞLIYORUZ!")
    i = 0
    benim_puanim = 0
    bilgisayar_puani = 0
    while i < 5:
        secenekler = ("taş", "kağıt", "makas")
        bilgisayar_secimi = random.choice(secenekler)
        query = takeCommand().lower()
        if query == "taş":
            if bilgisayar_secimi == "taş":
                speak("Taş")
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            elif bilgisayar_secimi == "kağıt":
                speak("Kağıt")
                bilgisayar_puani += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            else:
                speak("Makas")
                benim_puanim += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
        elif query == "kağıt":
            if bilgisayar_secimi == "taş":
                speak("Taş")
                benim_puanim += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            elif bilgisayar_secimi == "kağıt":
                speak("Kağıt")
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            else:
                speak("Makas")
                bilgisayar_puani += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
        elif query == "makas":
            if bilgisayar_secimi == "taş":
                speak("Taş")
                bilgisayar_puani += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            elif bilgisayar_secimi == "kağıt":
                speak("Kağıt")
                benim_puanim += 1
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
            else:
                speak("Makas")
                print(f"Skor:- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
        else:
            speak("Geçersiz seçim, lütfen taş, kağıt veya makas deyin.")
            i -= 1  # Do not count invalid input
        i += 1
    print(f"SON SKOR :- Ben :- {benim_puanim} : Bilgisayar :- {bilgisayar_puani}")
