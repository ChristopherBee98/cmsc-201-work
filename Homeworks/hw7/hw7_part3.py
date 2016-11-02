#File: hw7_part3.py
#Author: Austin Bailey
#Date: 4/3/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Checks how many words, average word length, and sentences in a file.

def sentencesInFile(sentenceFile): #Calculates the amount of sentences in a file
    sentenceCount = 0
    myFile = open(sentenceFile, "r")
    entireFile = myFile.read()
    for g in range(0, len(entireFile)):
        if (entireFile[g] == '.'): #Checks for periods so it knows when sentences have ended
            sentenceCount += 1
    sentenceCount += 1
    myFile.close()
    return sentenceCount

def wordLengthInFile(lengthFile): #Calculates the average word length in a file
    totalLength = 0
    wordCount = 0
    myFile = open(lengthFile, "r")
    entireFile = myFile.read()
    entireFile = entireFile.strip()
    entireFile = entireFile.split() #Reduces the string to just a list of strings, so that the length and words can be both be counted
    for g in range(0, len(entireFile)):
        wordCount += 1
        totalLength += len(entireFile[g])
    averageLength = totalLength / wordCount #Calculates the average length
    myFile.close()
    return averageLength

def totalWordsInFile(wordFile): #Calculates the total words in a file
    wordCount = 0
    myFile = open(wordFile, "r")
    entireFile = myFile.read()
    entireFile = entireFile.strip()
    entireFile = entireFile.split() #Seperates all the words in the file
    for g in range(0, len(entireFile)):
        wordCount += 1
    myFile.close()
    return wordCount

def fileCheck(nameOfFile):
    tempFile = nameOfFile
    check1 = 0 #Checks for a valid file name
    while (check1 == 0):
        check2 = 0
        extensionCheck = '' #Checks for the extension to be correct
        for g in range(0, len(tempFile)):
            if (tempFile[g] == '.'): #Goes through the name until it reaches a period, after which the extension is recorded
                check2 += 1
            elif (check2 == 1):
                extensionCheck += tempFile[g] #Extension is recorded
        if ((extensionCheck == 'txt') or (extensionCheck == 'dat')): #Checks for the valid extension
            check1 += 1
            return tempFile
        else:
            print("Invalid format. Enter a valid filename. One with an .txt or .dat extension.")
            tempFile = str(input("Enter the name of the file to open: "))

def main():
    fileName = str(input("Enter the name of the file to open: "))
    trueFile = fileCheck(fileName)
    totalSentences = sentencesInFile(trueFile)
    wordLength = wordLengthInFile(trueFile)
    totalWords = totalWordsInFile(trueFile)
    print("Here is the amount of sentences in", trueFile, ":", totalSentences)
    print("Here is the length of the words in", trueFile, ":", wordLength)
    print("Here is the total word count in", trueFile, ":", totalWords)
main()
