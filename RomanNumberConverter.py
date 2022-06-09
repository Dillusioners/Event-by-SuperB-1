roman2 = input("Enter the roman number: ")
a = roman2.split()
a.reverse()
roman = ' '.join(a)
#10 => X
#50 => L
#100 => C
#1 => I

number = 0

for i in roman.upper():
    if i == "I":
        number = number + 1
    if i == "V":
        number = number + 5
    if i == "X":
        number = number + 10
    if i == "L":
        number = number + 50
    if i == "C":
        number = number + 100
    if i == "D":
        number = number + 500
    if i == "M":
        number = number + 1000

print(f'{roman2} to number is {number}')