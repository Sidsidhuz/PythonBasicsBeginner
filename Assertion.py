# syntax-->  assert condition message
#
import pyttsx3
def speak(text,lang='en'):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # engine.close()

def age(val):
    assert val > 0, 'Invalid age'
    print(f"{val} years old")
    speak(val)

def avg(val):
    assert len(val) > 0, 'ListIsEmpty'
    print(f"Average of the list is {sum(val) / len(val)}")

l = [1,2,3,4,5]


n = int(input("Enter the age :"))
age(n)
avg(l)