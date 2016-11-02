#File: hw2_part3.py
#Author: Austin Bailey
#Date: 2/12/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description This program performs question 12.

print("What is the price?")
price = float(input())
priceInDollars = int(price)
remainingCents = price - priceInDollars
realCents = int(remainingCents * 100)
print("The number of dollars is: $", priceInDollars)
print("The number of cents is: ", realCents)
