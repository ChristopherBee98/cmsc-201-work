#File: hw3_part4.py
#Author: Austin Bailey
#Date: 2/20/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will determine what state water is in.
FREEZING_POINT_IN_F = 32
FREEZING_POINT_IN_C = 0
BOILING_POINT_IN_F = 212
BOILING_POINT_IN_C = 100
def main():
    temperature = float(input("Please enter the temperature: "))
    typeOfTemperature = str(input("Please enter 'C' for Celsius, or 'F' for Fahrenheit: "))
    if (typeOfTemperature == 'F'):
        if (temperature >= 212):
            print("At this temperature, water is a gas.")
        elif (temperature <= 32):
            print("At this temperature, water is frozen.")
        else:
            print("At this temperature, water is a liquid.")
    elif (typeOfTemperature == 'C'):
        if (temperature >= 100):
            print("At this temperature, water is a gas.")
        elif (temperature <= 0):
            print("At this temperature, water is frozen.")
        else:
            print("At this temperature, water is a liquid.")
main()
