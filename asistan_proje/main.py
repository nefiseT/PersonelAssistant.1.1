import pyttsx3
import speech_recognition
import datetime
import requests
from bs4 import BeautifulSoup
import os
import random
import webbrowser
import pyautogui
from time import sleep
from pygame import mixer

language_mode = 'tr'  # default language mode

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

def set_voice_by_language(lang):
    global engine, voices
    # Try to find a voice matching the language code
    for voice in voices:
        if lang == 'tr' and ('turkish' in voice.name.lower() or 'turkish' in voice.id.lower()):
            engine.setProperty('voice', voice.id)
            return
        elif lang == 'en' and ('english' in voice.name.lower() or 'english' in voice.id.lower()):
            engine.setProperty('voice', voice.id)
            return
    # fallback to first voice
    engine.setProperty('voice', voices[0].id)

set_voice_by_language(language_mode)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Dinliyorum.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Anlaşıldı..")
        lang_code = 'en-IN' if language_mode == 'en' else 'tr-TR'
        query = r.recognize_google(audio, language=lang_code)
        print(f"input: {query}\n")
    except Exception as e:
        print("Tekrar eder misin?")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    # Password protection
    for i in range(3):
        a = input("Şifreyi giriniz :- ")
        pw_file = open("password.txt", "r")
        pw = pw_file.read().strip()
        pw_file.close()
        if a == pw:
            print("Merhaba, Asistan şaun dinleme modunda")
            break
        elif i == 2 and a != pw:
            exit()
        elif a != pw:
            print("Tekrar edin")

    while True:
        query = takeCommand().lower()

        if "başlat" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                if "arkaplan" in query:
                    speak("Arkaplanda bekliyor olacağım")
                    break

                elif "merhaba" in query:
                    speak("Merhaba, nasılsınız?")

                elif "iyiyim" in query:
                    speak("Bu harika")

                elif "nasılsın" in query:
                    speak("İyiyim, teşekkürler")

                elif "teşekkürler" in query:
                    speak("Rica ederim")

                elif "arat" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "hava durumu" in query or "derece" in query:
                    search = "sakarya'daki hava durumu"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"{search} şu anda {temp}")

                elif "saat" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Şu an saat {strTime}")

                elif "uyku" in query:
                    speak("Uyku modu")
                    exit()

                elif "aç" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "kapat" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "alarm kur" in query:
                    print("Zaman örneği giriniz: 10 ve 10 ve 10")
                    speak("Zamanı ayarla")
                    a = input("Lütfen zamanı söyleyin: ")
                    alarm(a)
                    speak("Tamamlandı")

                elif "durdur" in query:
                    pyautogui.press("k")
                    speak("Video durduruldu")

                elif "oynat" in query:
                    pyautogui.press("k")
                    speak("Video başladı")

                elif "sessiz" in query:
                    pyautogui.press("m")
                    speak("Video sessize alındı")

                elif "sesi artır" in query:
                    from keyboard import volumeup
                    speak("Ses artırıldı")
                    volumeup()

                elif "ses kıs" in query:
                    from keyboard import volumedown
                    speak("Ses kısıldı")
                    volumedown()

                elif "hatırlatma" in query:
                    rememberMessage = query.replace("hatırlat", "")
                    rememberMessage = rememberMessage.replace("asistan", "")
                    speak("Hatırlattığınız şey: " + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()

                elif "ne hatırlıyorsun" in query:
                    remember = open("Remember.txt", "r")
                    speak("Hatırlattığınız şey: " + remember.read())

                elif "favori şarkı" in query:
                    speak("Favori şarkılarınızı çalıyorum")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("#https://www.youtube.com/watch?v=b1frq7hqJcU")

                elif "haberler" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "hesapla" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("hesapla", "")
                    query = query.replace("asistan", "")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "sistemi kapat" in query:
                    speak("Sistemi kapatmak istediğinizden emin misiniz?")
                    shutdown = input("Bilgisayarınızı kapatmak istiyor musunuz? (evet/hayır) ")
                    if shutdown == "evet":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "hayır":
                        break

                elif "şifre değiştir" in query:
                    speak("Yeni şifre nedir?")
                    new_pw = input("Yeni şifreyi girin\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Tamamlandı")
                    speak(f"Yeni şifreniz {new_pw}")

                elif "günümü planla" in query:
                    tasks = []
                    speak("Eski görevleri temizlemek istiyor musunuz? (Lütfen EVET veya HAYIR deyin)")
                    query = takeCommand().lower()
                    if "evet" in query:
                        file = open("tasks.txt", "w")
                        file.write("")
                        file.close()
                        no_tasks = int(input("Görev sayısını girin: "))
                        for i in range(no_tasks):
                            tasks.append(input("Görevi girin: "))
                        file = open("tasks.txt", "a")
                        for i in range(no_tasks):
                            file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                    elif "hayır" in query:
                        no_tasks = int(input("Görev sayısını girin: "))
                        for i in range(no_tasks):
                            tasks.append(input("Görevi girin: "))
                        file = open("tasks.txt", "a")
                        for i in range(no_tasks):
                            file.write(f"{i}. {tasks[i]}\n")
                        file.close()

                elif "planımı göster" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    from plyer import notification
                    notification.notify(
                        title="Görevleriniz:",
                        message=content,
                        timeout=15
                    )

                elif "aç" in query:
                    query = query.replace("aç", "")
                    query = query.replace("asistan", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet hızı" in query:
                    import speedtest
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1048576
                    download_net = wifi.download() / 1048576
                    print("Wifi Yükleme Hızı:", upload_net)
                    print("Wifi İndirme Hızı:", download_net)
                    speak(f"Wifi indirme hızı {download_net}")
                    speak(f"Wifi yükleme hızı {upload_net}")

                elif "ipl skoru" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
                    print(f"{team1} : {team1_score}")
                    print(f"{team2} : {team2_score}")
                    notification.notify(
                        title="IPL SKORU:",
                        message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
                        timeout=15
                    )

                elif "oyun oyna" in query:
                    from game import game_play
                    game_play()

                elif "ekran görüntüsü" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "fotoğraf çek" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("kamera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("GÜLÜMSE")
                    pyautogui.press("enter")

                elif "odak modu" in query:
                    a = int(input("Odak moduna girmek istediğinizden emin misiniz? :- [1 EVET / 2 HAYIR] "))
                    if a == 1:
                        speak("Odak moduna giriliyor....")
                        os.startfile("FocusMode.py")
                        exit()
                    else:
                        pass

                elif "odak göster" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "çevir" in query:
                    from Translator import translategl
                    query = query.replace("asistan", "")
                    query = query.replace("çevir", "")
                    translategl(query)

        elif "turkce moduna geç" in query:
            language_mode = 'tr'
            set_voice_by_language(language_mode)
            speak("Türkçe moduna geçildi")

        # Disabled English mode switching to enforce full Turkish mode
        # elif "switch to english" in query:
        #     language_mode = 'en'
        #     set_voice_by_language(language_mode)
        #     speak("Switched to English mode")
