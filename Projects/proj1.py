#File: proj1.py
#Author: Austin Bailey
#Date: 4/8/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Make a saveable game of tic tac toe.

UNDECIDED_WINNER = 0
YES = 1
NO = 2
WIN = 1
TIE = 2

import random

#playAgain() determines whether the player wants to play again
#Input: decision from player
#Output: yes or no depending on their response
def playAgain(decision):
    if (decision == "Y" or decision == "YES"):
        return YES
    elif (decision == "N" or decision == "NO"):
        return NO

#isWin() checks to see if there is a winner and returns a value related to it
#Input: the current board
#Output: a value that checks whether a winner has been found
def isWin(isWinCount, activeSymbol):
    if (isWinCount[0] == activeSymbol and isWinCount[1] == activeSymbol and isWinCount[2] == activeSymbol):
        return WIN
    elif (isWinCount[3] == activeSymbol and isWinCount[4] == activeSymbol and isWinCount[5] == activeSymbol):
        return WIN
    elif (isWinCount[6] == activeSymbol and isWinCount[7] == activeSymbol and isWinCount[8] == activeSymbol):
        return WIN
    elif (isWinCount[0] == activeSymbol and isWinCount[3] == activeSymbol and isWinCount[6] == activeSymbol):
        return WIN
    elif (isWinCount[1] == activeSymbol and isWinCount[4] == activeSymbol and isWinCount[7] == activeSymbol):
        return WIN
    elif (isWinCount[2] == activeSymbol and isWinCount[5] == activeSymbol and isWinCount[8] == activeSymbol):
        return WIN
    elif (isWinCount[0] == activeSymbol and isWinCount[4] == activeSymbol and isWinCount[8] == activeSymbol):
        return WIN
    elif (isWinCount[2] == activeSymbol and isWinCount[4] == activeSymbol and isWinCount[6] == activeSymbol):
        return WIN
    elif ((isWinCount[0] == "X" or isWinCount[0] == "O") and (isWinCount[1] == "X" or isWinCount[1] == "O") and (isWinCount[2] == "X" or isWinCount[2] == "O") and (isWinCount[3] == "X" or isWinCount[3] == "O") and (isWinCount[4] == "X" or isWinCount[4] == "O") and (isWinCount[5] == "X" or isWinCount[5] == "O") and (isWinCount[6] == "X" or isWinCount[6] == "O") and (isWinCount[7] == "X" or isWinCount[7] == "O") and (isWinCount[8] == "X" or isWinCount[8] == "O")):
        return TIE
    else:
        return UNDECIDED_WINNER

#loadCount() loads the saved count
#Input: none
#Output: the saved count
def loadCount():
    countFile = open("tic.txt", "r")
    listOfData = countFile.readlines()
    #sets the count equal to the one in tic.txt
    count = listOfData[7]
    count = count.split()
    countFile.close()
    return count

#loadBoard() loads the saved board
#Input: none
#Output: the saved board
def loadBoard():
    boardFile = open("tic.txt", "r")
    listOfData = boardFile.readlines()
    for g in range(0, 5):
        board += listOfData[g]
    boardFile.close()
    return board

#loadPlayer() loads the saved turn
#Input: none
#Output: the saved turn
def loadPlayer():
    playerFile = open("tic.txt", "r")
    listOfData = playerFile.readlines()
    player = listOfData[5]
    #verifies which player it is since it is a string and not a integer
    if (player == "1"):
        player = 1
        playerFile.close()
        return player
    else:
        player = 2
        playerFile.close()
        return player

#loadSymbol() is where the saved symbol is loaded
#Input: none
#Output: saved symbol
def loadSymbol():
    symbolFile = open("tic.txt", "r")
    listOfData = symbolFile.readlines()
    symbol = listOfData[6]
    symbolFile.close()
    return symbol

#saveFeature() is where the board, player, symbol, and count are saved to tic.txt
#Input: board, player, symbol, and count
#Output: none
def saveFeature(boardToSave, playerToSave, symbolToSave, countToSave):
    savedPlayer = str(playerToSave)
    savedCount = ' '.join(countToSave)
    myFile = boardToSave + "\n" + savedPlayer + "\n" + symbolToSave + "\n" + savedCount
    savedFile = open("tic.txt", "w")
    savedFile.write(myFile)
    savedFile.close()

#addSymbolBoard() is where the symbols are added to the board
#Input: the current board
#Output: the board with the respective mark is sent out
def addSymbolBoard(returnBoard, returnSymbol, returnChoice):
    choice = str(returnChoice)
    returnBoard = returnBoard.replace(choice, returnSymbol)
    return returnBoard

#addSymbolCount() updates the list of numbers used to create the board
#Input: the current count, the current symbol, and the active choice
#Output: the newly formed list
def addSymbolCount(returnCount, returnSymbol, returnChoice):
    choice = str(returnChoice)
    count = ' '.join(returnCount)
    count = count.replace(choice, returnSymbol)
    count = count.split()
    return count

#boardModifier() is where the board is changed, saved or loaded
#Input: the initial board, the first player, and the first players symbol
#Output: multiple different boards that are changed, saved, or loaded
def boardModifier(changingBoard, currentPlayer, currentSymbol, currentCount):
    checkWinner = UNDECIDED_WINNER
    playerCheck = currentPlayer
    while (checkWinner == UNDECIDED_WINNER):
        #sets the board equal to the current board before attempted modification
        boardCheck = changingBoard
        print("Player " + str(currentPlayer) + ", what is your choice?")
        choice = int(input("Enter 1-9 to mark, -1 to save, and -2 to load: "))
        if ((choice <= 9 and choice >= 1) or (choice == -1) or (choice == -2)):
            if (choice <= 9 and choice >= 1):
                changingBoard = addSymbolBoard(changingBoard, currentSymbol, choice)
                currentCount = addSymbolCount(currentCount, currentSymbol, choice)
                #checks to see if the board is the same as the one before the attempted change
                if (changingBoard == boardCheck):
                    print("That space is already taken.")
                    print("")
                else:
                    checkWinner = isWin(currentCount, currentSymbol)
                    if (checkWinner == WIN):
                        play = str(input("Player " + str(currentPlayer) + " has won! Play again?: "))
                        play = play.upper()
                        if (playAgain(play) == YES):
                            checkWinner += 1
                            main()
                        elif (playAgain(play) == NO):
                            checkWinner += 1
                            print("Thanks for playing!")
                    elif (checkWinner == TIE):
                        play = str(input("Game ended in tie. Play again?: "))
                        play = play.upper()
                        if (playAgain(play) == YES):
                            checkWinner += 1
                            main()
                        elif (playAgain(play) == NO):
                            print("Thanks for playing!")
                            checkWinner += 1
                    else:
                        #checks for player verification
                        playerCheck += 1
                        if (playerCheck % 2 == 0):
                            currentPlayer = 2
                            if (currentSymbol == "X"):
                                currentSymbol = "O"
                                print(changingBoard)
                                print("")
                            else:
                                currentSymbol = "X"
                                print(changingBoard)
                                print("")
                        else:
                            currentPlayer = 1
                            if (currentSymbol == "X"):
                                currentSymbol = "O"
                                print(changingBoard)
                                print("")
                            else:
                                currentSymbol = "X"
                                print(changingBoard)
                                print("")
            if (choice == -1):
                saveFeature(changingBoard, currentPlayer, currentSymbol, currentCount)
                play = str(input("Game has been saved. Play again?: "))
                play = play.upper()
                if (playAgain(play) == YES):
                    checkWinner += 1
                    #calls main for a redo of the game
                    main()
                elif (playAgain(play) == NO):
                    print("Thanks for playing!")
                    checkWinner += 1
            if (choice == -2):
                print("The game has been loaded.")
                changingBoard = loadBoard()
                currentSymbol = loadSymbol()
                currentCount = loadCount()
                currentPlayer = loadPlayer()
                print(changingBoard)
    
#boardCreator() creates the tic tac toe board
#Input: initial count
#Output: the initial board
def boardCreator(initialCount):
    board = ""
    #goes through the count list to make the board
    for g in initialCount:
        board += g
        if (g == "3" or g == "6"):
            board += "\n-----\n"
        #prevents the line from being placed at the end of the 9
        elif (g == "9"):
            return board
        else:
            board += "|"

def main():
    print("Welcome to Tic-Tac-Toe")
    print("This game is made for 2 players")
    #randomly assigns first player
    player = random.randint(1, 2)
    #randomly assigns the first players symbol
    symbol = random.randint(1, 2)
    if (symbol == 1):
        symbol = "X"
    elif (symbol == 2):
        symbol = "O"
    print("Player " + str(player) + " will go first and will play with the " + symbol)
    #sets the board created in boardCreator to currentBoard
    count = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentBoard = boardCreator(count)
    print(currentBoard)
    boardModifier(currentBoard, player, symbol, count)
main()
