while True:
    a = int(input("Enter a number you want to check is prime number or not: \n"))
    def is_prime(a):
        if a%a==0 and a<10 and a/4!=1 and a/6!=1 and a/9!=1 and a/8!=1:
            print(f"{a} is a prime number")
        elif a%a==0 and a%2!=0 and a%3!=0 and a%4!=0 and a%5!=0 and a%6!=0 and a%7!=0 and a%8!=0 and a%9!=0:
            print(f"{a} is a prime number")
        else:
            print(f"{a} is not a prime number")

    is_prime(a)
        
