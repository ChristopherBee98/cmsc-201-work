#File: hw3_part5.py
#Author: Austin Bailey
#Date: 2/20/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will calculate a day of the week.

def main():
    dayOfMonth = int(input("Please enter the day of the month: "))
    if (dayOfMonth > 31):
        print("Invalid day.")
    elif (dayOfMonth <= 0):
        print("Invalid day.")
    elif (dayOfMonth <= 7):
        if (dayOfMonth == 1):
            print("Today is a Monday!")
        elif (dayOfMonth == 2):
            print("Today is a Tuesday!")
        elif (dayOfMonth == 3):
            print("Today is a Wednesday!")
        elif (dayOfMonth == 4):
            print("Today is a Thursday!")
        elif (dayOfMonth == 5):
            print("Today is a Friday!")
        elif (dayOfMonth == 6):
            print("Today is a Saturday!")
        elif (dayOfMonth == 7):
            print("Today is a Sunday!")
    else:
        if (dayOfMonth % 7 == 1):
            print("Today is a Monday!")
        elif (dayOfMonth % 7 == 2):
            print("Today is a Tuesday!")
        elif (dayOfMonth % 7 == 3):
            print("Today is a Wednesday!")
        elif (dayOfMonth % 7 == 4):
            print("Today is a Thursday!")
        elif (dayOfMonth % 7 == 5):
            print("Today is a Friday!")
        elif (dayOfMonth % 7 == 6):
            print("Today is a Saturday!")
        elif (dayOfMonth % 7 == 7):
            print("Today is a Sunday!")
main()
        
