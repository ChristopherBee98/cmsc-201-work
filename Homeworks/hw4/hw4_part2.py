#File: hw4_part2.py
#Author: Austin Bailey
#Date: 2/27/2016
#Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will print every third letter of a string.

def main():
    stringInput = str(input("Please enter a sentence: "))
    stringLength = len(stringInput)
    print("Original sentence: ")
    print(stringInput)
    print("Every third letter: ")
    newSentence = ''
    for g in range(0, stringLength, 3):
        newSentence += stringInput[g]
    print(newSentence)
main()
