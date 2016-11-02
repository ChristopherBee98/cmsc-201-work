#File: hw6_part1.py
#Author: Austin Bailey
#Date: 3/25/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Program will read in numbers and add them to a list.

def main():
    check1 = 0 #Creates a counter to check when the list length reaches 8
    List = []
    firstNumber = int(input("Please enter a number: ")) #Creates the first number in the list, so the list isn't empty when it reaches the while loop
    List.append(firstNumber) #Appends the first number
    while (check1 == 0):
        check2 = 0 #Creates a counter to check for whether the same number has been entered is in the list
        inputNumber = int(input("Please enter a number: ")) 
        for g in range(0, len(List)):
            if (List[g] != inputNumber): #Checks if the current number is the same as the input
                check2 += 1 #If it isn't, it's updating the counter
                if (check2 == len(List)): #If the entire list has been checked and the same number hasn't been found, the number is then appended
                    List.append(inputNumber)
                    if (len(List) == 8): #Ends the while loop when the maximum allowed size of the list is reached
                        check1 += 1
            elif (List[g] == inputNumber): #At any point if a duplicate number is found, the for loop ends
                print("The number " + str(List[g]) + " is already in the list.")
    print("The contents of the list are: ")
    for h in range(0, len(List)): #Prints out the contents after the list has been completed
        print(List[h])
main()
