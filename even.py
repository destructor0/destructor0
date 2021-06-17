def for_even(li):
    count = 0
    for i in li:
        if i % 2 ==0:
            count+=1
    print(count)
for_even([1, 2, 3, 4])