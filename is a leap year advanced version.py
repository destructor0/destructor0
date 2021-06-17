from pyttsx3 import speak

while True:
    a = int(input(""))
    def is_leap():
        if a%4==0 and (a%100!=0 or a%400==0):
            return True
        else:
            return False

    if is_leap()== True:
        speak(f"{a} is a leap year")
    else:
        speak(f"{a} is not a leap year")