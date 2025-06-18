import pyttsx3
def speak_pyttsx3(text, language):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.close()
def Welcome(a):
    speak_pyttsx3("Welcome Employee " + a, language='eng')
