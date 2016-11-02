#File: hw5_part2.py
#Author: Austin Bailey
#Date: 3/4/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Cost of copies at UMBC.
FIRST_PRICE = 0.08
SECOND_PRICE = 0.06
THIRD_PRICE = 0.05
FOURTH_PRICE = 0.04

def main():
    amountOfCopies = int(input("How many copies do you want? "))
    copyTracker = 0
    totalAmount = 0
    if (amountOfCopies <= 100):
        totalAmount = amountOfCopies * FIRST_PRICE       
    elif ((amountOfCopies > 100) and (amountOfCopies <= 1000)):
        someAmount = amountofCopies - 100
        totalAmount1 = 100 * FIRST_PRICE
        totalAmount2 = someAmount * SECOND_PRICE
        totalAmount = totalAmount1 + totalAmount2
    elif ((amountOfCopies > 1000) and (amountOfCopies  <= 10000)):
        someAmount = amountOfCopies - 1000
        totalAmount1 = 100 * FIRST_PRICE
        totalAmount2 = 900 * SECOND_PRICE
        totalAmount3 = someAmount * THIRD_PRICE
        totalAmount = totalAmount1 + totalAmount2 + totalAmount3
    elif (amountOfCopies > 10000):
        someAmount = amountOfCopies - 10000
        totalAmount1 = 100 * FIRST_PRICE
        totalAmount2 = 900 * SECOND_PRICE
        totalAmount3 = 9000 * THIRD_PRICE
        totalAmount4 = someAmount * FOURTH_PRICE
        totalAmount = totalAmount1 + totalAmount2 + totalAmount3 + totalAmount4
    print("The total cost for",amountOfCopies,"copies is $"+str(totalAmount))
main()
