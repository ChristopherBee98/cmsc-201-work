#File: hw8_part3.py
#Author: Austin Bailey
#Date: 4/24/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Will build a list of unique characters from a file.

#newChar() is a recursive function that will single out all unique characters
#Input: the file string, the character list, the counter, and the file itself
#Output: the character list
def newChar(fileString, storeList, fileCounter, myFile):
    check = 0
    if fileCounter != (len(myFile) - 1):
        for g in storeList:
            if g == fileString:
                check += 1
        if check > 0:
            fileCounter += 1
            newChar(myFile[fileCounter], storeList, fileCounter, myFile)
        else:
            storeList.append(fileString)
            fileCounter += 1
            newChar(myFile[fileCounter], storeList, fileCounter, myFile)
    else:
        return storeList

def main():
    listToSend = []
    counter = 0
    basicFile = open("input.txt")
    stringFile = basicFile.read()
    listToSend.append(stringFile[counter])
    newChar(stringFile[counter], listToSend, counter, stringFile)
    print(listToSend)
    basicFile.close()
main()
