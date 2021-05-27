# Write a program that prompts the user to input a character and determine
# the character is vowel or consonant

letter = input("Enter a letter : ")

if letter == 'a' or letter == 'i' or letter == 'e' or letter == 'o' or letter == 'u':
    print(letter, "is Vowel")

else:
    print(letter, "is Consonant")
