word = input("Enter the word you want to check")
while word == "":
    word = input("Enter the word again correctly")
last_one_lad = word[:: -1]
if last_one_lad == word:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome...its reverse is",last_one_lad)
    