#File: proj2.py
#Author: Austin Bailey
#Date: 4/26/16
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: This program will search through a word puzzle and find certain words.

#determineWords(...) determines whether the given letter leads to an actual word
#Input: the puzzle, list of words, the current word position, and current puzzle position
#Output: gives either the direction of the word or a nada for letting the other function know that it doesn't lead to a word
def determineWords(determinePuzzle, determineWordList, counter1, counter2, tempCounter):
    for a in range(0, len(determinePuzzle[counter1])):
        if determinePuzzle[counter1][a] == determineWordList[counter2][tempCounter]:
            if determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1+1][a]:
                return "bottom"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1][a-1]:
                return "left"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1-1][a]:
                return "up"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1][a+1]:
                return "right"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1+1][a-1]:
                return "bottomleft"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1+1][a+1]:
                return "bottomright"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1-1][a+1]:
                return "upright"
            elif determineWordList[counter2][tempCounter-1] == determinePuzzle[counter1-1][a-1]:
                return "upleft"
            else:
                return "nada"
        elif a == determinePuzzle[counter1][(len(determinePuzzle[counter1]) - 1)]:
            counter += 1

#findWords(listPuzzle) finds the possible beginning of words in the 2d puzzle
#Input: the 2d puzzle, and the list of words
#Output: a possible word beginning of a word which is sent to the function determineWords
def findWords(listPuzzle, listWords, counter1, counter2):
    tempCounter = 1
    for a in listPuzzle[counter1]:
        if a == listWords[counter2][0]:
            whichDirection = determineWords(listPuzzle, listWords, 0, counter2, tempCounter)
            if whichDirection == "nada":
                print("It does not appear in the puzzle.")
            elif whichDirection == "upleft":
                print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes diagonally up and to the left")
            elif whichDirection == "left":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes to the left")
            elif whichDirection == "bottomleft":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes diagonally down to the left")
            elif whichDirection == "bottom":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes down")
            elif whichDirection == "bottomright":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes diagonally down to the right")
            elif whichDirection == "right":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes to the right")
            elif whichDirection == "upright":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes diagonally up and to the right")
            elif whichDirection == "up":
                 print("The word " + listWords[counter2] + " appears at " + str(counter1) + ", " + str(counter2) + " and goes up")
        elif a == listPuzzle[counter1][(len(listPuzzle[counter1]) - 1)]:
            counter1 += 1

#returnPuzzle(puzzleFile) creates the 2d puzzle that will or will not have certain words
#Input: the text file containing the puzzle
#Output: the 2d puzzle
def returnPuzzle(puzzleFile):
    myFile = open(puzzleFile)
    tempPuzzle = myFile.readlines()
    for g in range(0, len(tempPuzzle)):
        tempPuzzle[g] = tempPuzzle[g].strip()
    myFile.close()
    return tempPuzzle

#listOfWords(wordFile) creates the list of words used to search for in the puzzle
#Input: the text file containing the words
#Output: the list of words
def listOfWords(wordFile):
    myFile = open(wordFile)
    tempWord = myFile.readlines()
    for g in range(0, len(tempWord)):
        tempWord[g] = tempWord[g].strip()
    myFile.close()
    return tempWord

def main():
    counter1 = 0
    counter2 = 0
    print("Welcome to the Word Search!")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")
    wordList = str(input("What is the word list file you would like to import?: "))
    puzzleList = str(input("What is the puzzle file you would like to import?: "))
    setWords = listOfWords(wordList)
    setPuzzle = returnPuzzle(puzzleList)
    while counter2 != len(setWords):
        findWords(setPuzzle, setWords, counter1, counter2)
        counter2 += 1
main()
