#File: lab10.py
#Author: Austin Bailey
#Date: 4/19/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program will abbreviate state names.

def convertToDict(fileContents):
    stateDict = {}
    fileContents = fileContents.readlines()
    for line in fileContents:
        pair = line.split(",")
        stateDict[pair[0]] = pair[1]
    return stateDict
def main():
    states = open("states.txt")
    stateDictionary = convertToDict(states)
    print("Welcome to the State Abbreviator")
    word = ""
    while (word != 'exit'):
        word = str(input("Please enter the state to abbreviate list to get list and exit to exit: "))
        if word == 'list':
            print(stateDictionary.keys())
        elif word in stateDictionary:
            print("The abbreviation of the state: " + word + " is " + stateDictionary[word])
        elif word == 'exit':
            print("")
        else:
            print("That isn't a state.")
    print("Thank you for using the state abbreviator!")
main()
