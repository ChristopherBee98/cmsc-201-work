#File: palindrome.py
#Author: Austin Bailey
#Date: 3/1/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Program will determine what is a palindrome.

def main():
    stringInput = str(input("Enter a string: "))
    stringLength = len(stringInput) - 1
    reverseString = ''
    for g in range(stringLength, -1, -1):
        reverseString += stringInput[g]
    if (reverseString == stringInput):
        print(stringInput, "is a palindrome.")
    else:
        print(stringInput, "is not a palindrome.")
main()
