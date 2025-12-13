import speech_recognition as sr

def list_microphones():
    print("Available microphone devices:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")

def test_microphone(device_index=None):
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=device_index) as source:
            print("Microphone is accessible. Say something:")
            audio = r.listen(source, timeout=5)
            print("Audio captured successfully.")
    except Exception as e:
        print(f"Error accessing microphone: {e}")

if __name__ == "__main__":
    list_microphones()
    # You can specify device_index if needed, e.g. test_microphone(0)
    test_microphone()
