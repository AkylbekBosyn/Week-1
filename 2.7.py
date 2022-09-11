def printing(letter,number):
    print(letter * number)
word = str(input("Enter the word "))
number = int(input("Enter the number "))
word = tuple(word)
for letters in word:
    printing(letters , number)
