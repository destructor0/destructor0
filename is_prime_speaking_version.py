from pyttsx3 import speak as Sp
Sp("type a number you want to check is prime or not")
try:    
    while True:
        a = int(input("Number here:\n"))
        def is_prime(a):
            
                if a%a==0 and a<10 and a/4!=1 and a/6!=1 and a/9!=1 and a/8!=1:
                    Sp(f"{a} is a prime number")
                elif a%a==0 and a%2!=0 and a%3!=0 and a%4!=0 and a%5!=0 and a%6!=0 and a%7!=0 and a%8!=0 and a%9!=0:
                    Sp(f"{a} is a prime number")
                else:
                    Sp(f"{a} is not a prime number")

      
        is_prime(a)
except Exception as e:
    
    Sp("Because you didn't entered a number this program crashed")
    print(e)