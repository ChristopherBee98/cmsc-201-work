#File: milesPerWeek.py
#Author: Austin Bailey
#Date: 2/16/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program is going to calculate how many miles you commute per week.
carSpeed = 65
def main():
    milesPerTrip = int(input("How many miles is the trip one-way?"))
    numberOfTrips = int(input("How many days a week do you go to work?"))
    totalMiles = milesPerTrip * 2 * numberOfTrips
    hoursInCar = totalMiles / carSpeed
    print("The number of miles you drive in a typical week is:", totalMiles)
    print("The number of hours spent in the car in a typical week is:", hoursInCar)

main()
