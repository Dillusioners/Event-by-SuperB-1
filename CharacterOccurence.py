word = input("Enter the word: ")
letters = []
for i in word:
    if i != " ":
        letters.append(i)
print("The number of characters in this word is ", len(letters))