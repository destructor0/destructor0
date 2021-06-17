invested = int(input("Enter the amount of money you have invested: "))
years = int(input("Time in years: "))
if years==1:
    print(float(invested*0.075+invested))
elif years==2:
    print(float(invested*0.075*2+invested))
elif years==5:
    print(float(invested*0.075*5+invested))
elif years==10:
    print(float(invested*0.75+invested))

