import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

from main import language_mode
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        if language_mode == 'tr':
            speak("Google'da bulduklarım")
        else:
            speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            if language_mode == 'tr':
                speak("Konuşulabilir sonuç bulunamadı")
            else:
                speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        if language_mode == 'tr':
            speak("Aramanız için bulduklarım")
        else:
            speak("This is what I found for your search!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        if language_mode == 'tr':
            speak("Tamamdır efendim")
        else:
            speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        if language_mode == 'tr':
            speak("Wikipedia'dan arıyorum....")
        else:
            speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        if language_mode == 'tr':
            speak("Wikipedia'ya göre..")
        else:
            speak("According to wikipedia..")
        print(results)
        speak(results)
