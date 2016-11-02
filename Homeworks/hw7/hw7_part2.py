#File: hw7_part2.py
#Author: Austin Bailey
#Date: 4/3/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Converting UMBC dollars.
RETRIEVER_BUX = 0.125 #Amount of retriever bux per us dollar
US_DOLLAR = 8 #Amount of us dollars per retriever bux

def usaToRetriever(amountUSA): #Calculates the conversion from usa to retriver dollars
    newAmount = amountUSA * US_DOLLAR #Calculates the amount of retriever bux
    newAmount = format(newAmount, '.2f') #Formats the variable so it has 2 decimal places
    print("Amount of Retriever Bux is: ", newAmount)
    print("Thanks for using Currency Converter!") 

def retrieverToUsa(amountRetriever): #Calculates the conversion rate from retriever to us dollars
    newAmount = amountRetriever * RETRIEVER_BUX #Calculates the amount of us dollars
    newAmount = format(newAmount, '.2f')
    print("Amount of US Dollars is: ", newAmount)
    print("Thanks for using Currency Converter!")

def main():
    check = 0 #Checks for the valid choice
    print("Welcome to the Currency Converter!")
    print("What would you like to do?")
    print("1. Convert US Dollars to Retriever Bux")
    print("2. Convert Retriever Bux to US Dollars")
    print("3. Exit")
    while (check == 0):
        choice = int(input("Enter your choice: "))
        if ((choice > 3) or (choice < 1)): #Checks to see if you chose a valid number
            print("Invalid choice.")
        else:
            check += 1
    if (choice == 1):
        money = float(input("How much do you want to convert? "))
        usaToRetriever(money)
    elif (choice == 2):
        money = float(input("How much do you want to convert? "))
        retrieverToUsa(money)
    else:
        print("Thanks for using Currency Converter!")
main()
