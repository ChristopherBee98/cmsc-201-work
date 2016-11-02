#File: hw8_part1.py
#Author: Austin Bailey
#Date: 4/22/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Takes in positive integers and adds them up.

#maxFind(maxList) finds the max number
#Input: the full list
#Output: the max number in the list
def maxFind(maxList):
    maxNum = maxList[0]
    for g in maxList:
        if g > maxNum:
            maxNum = g
    return maxNum

#maxInt(currentList) creates the list
#Input: the empty list
#Output: the full list
def maxInt(currentList):
    addNumber = int(input("Enter a number to append to the list, or -1 to stop: "))
    if addNumber >= 0:
        currentList.append(addNumber)
        maxInt(currentList)
    elif addNumber == -1:
        return currentList
    else:
        maxInt(currentList)

def main():
    totalList = []
    maxInt(totalList)
    print("The list you entered is: ", totalList)
    maxNumber = maxFind(totalList)
    print("The maximum number in the list is: ", maxNumber)
main()
