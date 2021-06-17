import pyttsx3           
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    dates = (datetime.datetime.now().day)
    months = (datetime.datetime.now().month)
    if months == 1:
        months = "January"
    elif months == 2:
        months = "february"
    elif months == 3:
        months = "March"
    elif months == 4:
        months = 'April'
    elif months == 5:
        months = 'May'
    elif months == 6:
        months = 'june'
    elif months == 7:
        months = 'july'
    elif months == 8:
        months = 'August'
    elif months == 9:
        months = 'September'
    elif months == 10:
        months = 'October'
    elif months == 11:
        months = 'November'
    else:
        months = 'December'
    if hour>= 0 and hour<12:
        speak("Good morning! Deepjal")
    elif hour>=12 and hour <18:
        speak("Good Afternoon! Deepjal")
    else:
        speak("good evening! Deepjal")
    #speak("I am a girl and i can't hear you because Speech Recognition module isn't installed yet")
    speak(f"Today's date is {dates}th {months} and time right now is {hour} {minute}")

#if __name__ == "__main__":
wish_me()


