import pyttsx3
def speak_pyttsx3(text, language):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def Boss_Hai():
    speak_pyttsx3("Hai Boss", language="mal")


