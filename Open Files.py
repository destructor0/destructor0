from pyttsx3 import speak as S
import os
while True:
    a = input(S("Type code for your app"))
    if a=="VS":
        path = "E:\pps shortcuts\Code"
        S(f"Opening Visual Studio Code")
        os.startfile(path)
    elif a=="Ch":
        path = "E:\pps shortcuts\Google Chrome"
        S(f"Opening Chrome")
        os.startfile(path)

    elif a=="NSUNS4":
        path = "E:\\pps shortcuts\\NSUNS4"
        S("Opening Naruto Shippuden Ultimate Ninja Storm 4")
        os.startfile(path)


    else:
        S("Please type correctly")


