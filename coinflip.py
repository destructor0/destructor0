from random import randint as rn

def flip():   
    count = 0
    coun_1 = 0 
    while True:
        a = rn(1, 2)
        if a==2:
            count+=1
        else:
            coun_1+=1
        if count==100:
            b = count+coun_1
            print(f"If coin is flipped {b} times it will give 100 tails")
            exit()   
flip()
 