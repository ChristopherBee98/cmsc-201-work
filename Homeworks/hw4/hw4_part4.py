#File: hw4_part4.py
#Author: Austin Bailey
#Date: 2/27/2016
#Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will single out vowels.

def main():
    stringInput = str(input("Please enter a string: "))
    vowelTotal = 0
    for g in stringInput:
        if ((g == ('a' or 'e' or 'i' or 'o' or 'u' or 'y')) or (g == ('A' or 'E' or 'I' or 'O' or 'U' or 'Y'))):
            vowelTotal += 1
    print("There are", vowelTotal, "vowels in the string '" + stringInput + "'.")
main()
