#File: hw7_part1.py
#Author: Austin Bailey
#Date: 4/2/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program will convert phone numbers.

def convertLetter(number):
    for g in range(0, len(number)):
        myBool = number[g].isdigit()
        if (myBool == False):
            if (number[g] == 'A'):
                number.remove(number[g])
                number.insert(g, '2')
    return number
def main():
    print("Welcome to the Telephone Converter!")
    phoneNumber = str(input("Enter the phone number: "))
    newNumber = convertLetter(phoneNumber)
    print(newNumber)
main()

#Couldn't figure it out.
