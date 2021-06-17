#ask = input("What is the name of your dead animal? \n")
#ask1= input("Did it do good deeds or bad deeds? \n")
#if ask1 == "good deeds":
#    print(f"Now your {ask} will be fit and fine :)")
#elif ask1 == "bad deeds":
#    print(f"I am really sorry but it is not possible to revive, {ask} has done this much bad deeds:(")

#changing above program into talking program
import pyttsx3
a = input(pyttsx3.speak("What is the name of the animal\n"))
b = input(pyttsx3.speak("It has done good deeds or bad deeds?\n"))
if b == "good deeds":
    pyttsx3.speak(f"Phewwww! I am glad that {a} is now alive")
elif b == "bad deeds":
    pyttsx3.speak(f"Ohh no! {a} has done a lot of bad work so i think {a} deserves death")
elif b == "both":
    pyttsx3.speak("Then i will do what i can then the rest will be up to it. If it wills to live longer than it will live else it will die")
else:
    pyttsx3.speak("could you please type correctly good deeds for good work bad deeds for bad work and both if it has done both equally")
    
#congrats deepjal for completing it i am glad that you come this far and i believe that you are going to do great work and impress everyone from your good deeds indeed