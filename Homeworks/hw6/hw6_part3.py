#File: hw6_part3.py
#Author: Austin Bailey
#Date: 3/26/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program will build shapes.

def drawTriangle(number): #Draws the triangle
    for g in range(0, number):
        print("*" + (g * "*"))
    print("")
def drawParallelogram(number): #Draws the parallelogram
    counter = '*' * number #The line of astericks
    for g in range(0, number):
        if (g == 0): #For the first line
            print(counter)
        elif (g == 1): #For the possible second line
            print(' ' + counter)
        else: #Continues to add more and more spaces the larger the number
            print((g * ' ') + counter)
    print("")
def drawSquare(number): #Draws the square
    counter = '*' * number
    for g in range(0, number):
        print(counter) #Prints a line of astericks equal to the amount
    print("")
def main():
    check1 = 0 #For checking whether the person entered a positive integer
    check2 = 0 #For checking whether the person entered a valid name
    inputNumber = int(input("Please enter a positive integer: "))
    if (inputNumber <= 0):
        while (check1 == 0):
            inputNumber = int(input("Please enter a positive integer: "))
            if (inputNumber > 0):
                check1 += 1
    inputShape = str(input("Please choose the shape: square, parallelogram, triangle, or all: "))
    if (inputShape == 'square' or inputShape == 'parallelogram' or inputShape == 'triangle' or inputShape == 'all'):
        check2 += 1
    else:
        while (check2 == 0):
            inputShape = str(input("Please choose the shape: square, parallelogram, triangle, or all: "))
            if (inputShape == 'square' or inputShape == 'parallelogram' or inputShape == 'triangle' or inputShape == 'all'):
                check2 += 1
    if (inputShape == 'square'): #Each of these call their appropriate functions
        drawSquare(inputNumber)
    if (inputShape == 'parallelogram'):
        drawParallelogram(inputNumber)
    if (inputShape == 'triangle'):
        drawTriangle(inputNumber)
    if (inputShape == 'all'): #Calls all at once
        drawSquare(inputNumber)
        drawParallelogram(inputNumber)
        drawTriangle(inputNumber)
main()
