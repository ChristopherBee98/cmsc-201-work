#File: hw4_part1.py
#Author: Austin Bailey
#Date: 2/26/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will create a muliplication table.

def main():
    baseNumber = int(input("Enter the base number: "))
    maxNumber = int(input("Enter the max number: "))
    for g in range(0, maxNumber+1):
        print(str(baseNumber) + "*" + str(g) + "=" + str((g*baseNumber)))
main()
