import os
import time
words = ["CUM", "BANG", "MOTHER", "MILK", "DAD", "JOHNY", "BITCH"]
index1 = 1
for i in range(0, len(words)):
    if index1 == 1:
        print(f'The 1st word is {words[i]}')
        index1 = index1 + 1
    elif index1 == 2:
        print(f'The 2nd word is {words[i]}')
        index1 = index1 + 1
    elif index1 == 3:
        print(f'The 3rd word is {words[i]}')
        index1 = index1 + 1
    else:
        print(f'The {index1}th word is {words[i]}')
        index1 = index1 + 1

print("You have 5 seconds to remember those words.")
time.sleep(5)
os.system("cls")
print("5 seconds over, now tell the words 1 by 1.")
num1 = input("Enter the first word: ")
num2 = input("Enter the second word: ")
num3 = input("Enter the third word: ")
num4 = input("Enter the fourth word: ")
num5 = input("Enter the fifth word: ")
num6 = input("Enter the sixth word: ")
num7 = input("Enter the seventh word: ")

if(num1 == words[0]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[0])

if(num2 == words[1]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[1])

if(num3 == words[2]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[2])

if(num4 == words[3]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[3])

if(num4 == words[3]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[3])

if(num5 == words[4]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[4])

if(num6 == words[5]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[5])

if(num6 == words[5]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[5])

if(num7 == words[6]):
    print("You guessed the first word correct.")
else:
    print("The first word was ", words[6])
