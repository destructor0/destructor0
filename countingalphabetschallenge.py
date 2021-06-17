user = input("Enter your word, sentence or large text: ")
count = 0
for i in user:
    if i== "a" or i== "e" or i=="i" or i=="u" or i=="o":
        count += 1
l = len(user)-count
print(f"The number of vowels are {count}")
print(f"The number of consonants are {l}")