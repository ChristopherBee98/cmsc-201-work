#File: hw5_part3.py
#Author: Austin Bailey
#Date: 3/5/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Converting phone number to standard format.

def numberConversion(number):
    trueNumber = ''
    lengthNumber = len(number)
    if (lengthNumber == 13):
        for g in range(0, lengthNumber, 1):
            if (g == 5):
                trueNumber += ' '
            trueNumber += number[g]
        return trueNumber
    elif (lengthNumber == 12):
        for g in range(0, lengthNumber, 1):
            if (g == 3):
                trueNumber += ')'
                trueNumber += ' '
            elif (g != 3):
                if (g == 0):
                    trueNumber += '('
                trueNumber += number[g]
        return trueNumber
    elif (lengthNumber == 10):
        for g in range(0, lengthNumber, 1):
            if (g == 0):
                trueNumber += '('
            elif (g == 3):
                trueNumber += ')'
                trueNumber += ' '
            elif (g == 6):
                trueNumber += '-'
            trueNumber += number[g]
        return trueNumber
            
def main():
    phoneNumber = str(input("Please enter the phone number: "))
    correctNumber = numberConversion(phoneNumber)
    print("The formatted phone number is: "+correctNumber)
main()
