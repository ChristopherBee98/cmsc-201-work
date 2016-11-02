#File: hw4_part3.py
#Author: Austin Bailey
#Date: 2/27/2016
#Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will calculate plunges.

def main():
    pledgeAmount = int(input("How many pledges did you get? "))
    pledgeTotal = 0
    for g in range(1, pledgeAmount + 1):
        pledgeTotal += float(input("What is the value of donation " + str(g) + ": "))
    plungeAmount = int(input("How many plunges did you do? "))
    totalCharity = pledgeTotal * plungeAmount
    print("Based on your " + str(plungeAmount) + " plunges you earned $" + str(totalCharity) + " for the charity.")
main()
