#File: hw3_part1.py
#Author: Austin Bailey
#Date: 2/20/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will determine whether a number is positive or negative.

def main():
    inputNumber = float(input("Please enter a floating point number: "))
    if (inputNumber < 0):
        print("The number",inputNumber,"is negative.")
    elif (inputNumber > 0):
        print("The number",inputNumber,"is positive.")
    else:
        print("The number",inputNumber,"is equal to zero.")
main()
