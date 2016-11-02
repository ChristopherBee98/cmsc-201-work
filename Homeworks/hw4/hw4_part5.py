#File: hw4_part5.py
#Author: Austin Bailey
#Date: 2/27/2016
#Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This will do messages during intervals from 1 to 100.

def main():
    for g in range(1, 100):
        if ((g % 3 == 0) and (g % 5 == 0)):
            print("In the future, everyone will be world famous for 15 minutes.")
        elif (g % 5 == 0):
            print("Where do you see yourself in five years?")
        elif (g % 3 == 0):
            print("Better three hours too soon than a minute too late.")
        else:
            print(g)
main()
