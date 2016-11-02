#File: manners.py
#Author: Austin Bailey
#Date: 2/23/2016
#Section: 10
#Description: This program teaches manners.

def main():
    wordInput = str(input("Please enter a word: "))
    if ((wordInput == 'please') or (wordInput == 'thank you') or (wordInput == 'excuse me')):
        print("Your manners are impeccable.")
    else:
        print("How rude!")
main()
