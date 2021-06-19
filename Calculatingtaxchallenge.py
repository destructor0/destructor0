a = int(input("Cost of meal: "))
tip = float(15/100*a)
tax = float(10/100*a)
b = tip+tax
print(a-b)