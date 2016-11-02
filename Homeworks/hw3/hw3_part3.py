#File: hw3_part3.py
#Author: Austin Bailey
#Date: 2/20/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will let the user play a guess who like game.

def main():
    print("Please enter 'y' for yes and 'n' for no to these questions.")
    isWoman = str(input("Is your character a woman? (y/n) "))
    if (isWoman == 'y'):
        isBlueEyes = str(input("Does your character have blue eyes? (y/n) "))
        if (isBlueEyes == 'y'):
            print("Your character is Jane!")
        elif (isBlueEyes == 'n'):
            print("Your character is Marni!")
    if (isWoman == 'n'):
        isGlasses = str(input("Does your character wear glasses? (y/n) "))
        if (isGlasses == 'y'):
            print("Your character is Adrian!")
        elif (isGlasses == 'n'):
            isBeard = str(input("Does your character have a beard? (y/n) "))
            if (isBeard == 'y'):
                print("Your character is Peder!")
            elif (isBeard == 'n'):
                print("Your character is Zhang!")
main()

