def df():
    a = int(input("Price of order: "))
    if a<=100:
        b = 5+0.05*a
        print(f"Your delivery charge is {b}. Your order charge is {a} and your total bill is {a+b}")
    elif 100<a<=500:
        b = 10+0.02*a
        print(f"Your delivery charge is {b}. Your order charge is {a} and your total bill is {a+b}")
    elif a>500:
        b = 15+0.01*a
        print(f"Your delivery charge is {b}. Your order charge is {a} and your total bill is {a+b}")
df()