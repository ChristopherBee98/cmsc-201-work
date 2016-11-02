#File: hw8_part2.py
#Author: Austin Bailey
#Date: 4/22/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Make a square with some symbols.

#hollowSquare() creates the square of symbols
#Input: height, symbol, counter
#Output: square of symbols
def hollowSquare(height, symbol, counter):
    if (counter == 1 or counter == height):
        print(symbol * height)
        counter += 1
        hollowSquare(height, symbol, counter)
    elif 1 < counter < height:
        print(symbol + (' ' * (height - 2)) + symbol)
        counter += 1
        hollowSquare(height, symbol, counter)

def main():
    check = 0
    counterToSend = 1
    while check != 2:
        if check == 1:
            heightToSend = int(input("Please enter the height of the square (must be > 0): "))
            if heightToSend <= 0:
                check = 1
            else:
                check += 1
        else:
            heightToSend = int(input("Please enter the height of the square: "))
            if heightToSend <= 0:
                check += 1
            else:
                check += 2
    symbolToSend = str(input("Please enter a character for your square: "))
    hollowSquare(heightToSend, symbolToSend, counterToSend)
main()
