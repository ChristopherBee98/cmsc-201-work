#File: speeding.py
#Author: Austin Bailey
#Date: 2/23/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program is about speeding.

def main():
    speedLimit = int(input("Please enter the speed limit in MPH: "))
    drivingSpeed = int(input("Please enter the driving speed in MPH: "))
    overTheLimit = drivingSpeed - speedLimit
    print("You were over the speed limit by",overTheLimit," MPH.")
    if (overTheLimit < 5):
        print("You receive no ticket...this time.")
    elif (5 <= overTheLimit <= 15):
        print("You receive a ticket for a $100 fine.")
    elif (15 < overTheLimit < 30):
        print("You receive a ticket for a $200 fine.")
    elif (overTheLimit >= 30):
        print("You receive a ticket for a $500 fine, and a mandatory court date.")
main()
