#File: hw2_part2.py
#Author: Austin Bailey
#Date: 2/12/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description This program performs question 11.
TAX_PERCENTAGE = 0.065
SHIPPING_PRICE = 1.95

print("What is the price of the book?")
priceOfBook = float(input())
print("How many copies of this book would you like?")
quantityOfBooks = float(input())
tax = priceOfBook * TAX_PERCENTAGE
totalPriceOfBook = priceOfBook + tax
shippingCharge = quantityOfBooks * SHIPPING_PRICE
totalSum = (totalPriceOfBook * quantityOfBooks + shippingCharge)
print("Your total comes out to $", totalSum, ". Have a nice day!")
