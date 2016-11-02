#File: shopping.py
#Author: Austin Bailey
#Date: 3/8/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Shopping stuff.

def main():
    groceryList = []
    check = 0
    while (check == 0):
        newItem = str(input("Add item to list ('done' when finished): "))
        if (newItem == 'done'):
            check += 1
        else:
            groceryList.append(newItem)
    print("Final shopping list:", groceryList)
    totalPrice = 0
    while (0 < len(groceryList)):
        currentItem = groceryList[0]
        currentPrice = float(input("How much did " + currentItem + " cost?"))
        totalPrice += currentPrice
        groceryList.remove(currentItem)
    print("Your shopping trip cost $" + str(totalPrice))
    print("Shopping list at end of trip:", groceryList)
main()
