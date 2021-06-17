from pyttsx3 import speak as S
class House:
    def __init__(self, listOfMember):
        self.member = listOfMember

    def listingmembers(self):
        print("people in this house are\n")
        S("people in this house are\n")
        for member in self.member:
            print("*"+member)
            S("*"+member)

    def outofhouse(self, membername):
        if membername in self.member:
            self.member.remove(membername)
            S(f"{membername} has gone out for some work")
        else:
            S(f"Sorry {membername} is not in the house")
        
    def guest(self, membername):
        self.member.append(membername)
        S(f"Guest has came please greet {membername}")

    def rules(self):
        S("Rules in this house is there are no rules")
    
class member:
    def guestre(self):
        self.member = input(S("Enter name of your guest\n"))
        return self.member
    
    def Outre(self):
        self.member = input(S("If you are going out tell me your name\n"))
        return self.member

if __name__ == "__main__":
    My_house = House(["Deepjal", "Mother", "Father"])
    Memberss = member()
    welcome = '''===Welcome to my house===
    please choose an option
    1. list member
    2. go out of house
    3. for guests
    4. Rule of house
    5. exit
    '''
    print(welcome)
    S(welcome)
    while True:
        a = int(input("Enter your option\n"))
        if a==1:
            My_house.listingmembers()
        elif a==2:
            My_house.outofhouse(Memberss.Outre())
        elif a==3:
            My_house.guest(Memberss.guestre())
        elif a == 4:
            My_house.rules()
        elif a==5:
            S("Please visit my home again soon")
            exit()
        else:
            S("please type correctly")