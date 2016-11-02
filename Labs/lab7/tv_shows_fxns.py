# File:    tv_shows_fxns.py
# Author:  Austin Bailey
# Date:    3/29/16
# Section: 10
# E-mail:  baustin1@umbc.edu
# Description:
#   This file contains python code that implements lab5 (a 
#   TV show voting system) using functions to:
#   1) Get a choice
#   2) Find the name of the winner

STOP = 0

# getVote() returns a valid choice from the given list
# Input:    showList, a list of strings (names of shows to vote on)
# Output:   vote,     an integer containing a choice between 0 and list length
#          *reprompts user until valid choice is made*
def getVote(showList):
    ##################################################
    # your function to get the user's vote goes here #
    ##################################################
    vote = int(input("Press '0' to stop voting: "))
    return vote

# getWinner() takes in a list of shows and votes and calculates the winner
# Input:      showList, a list of strings (names of shows to vote on)
#             votes,    a list of integers (votes for each show)
# Output:     whoWon,   the name of the show that won with the most votes
#             *in case of a tie, the first show seen in the list wins*
def getWinner(showList, votes):
    ###################################################
    # your function to determine the winner goes here #
    ###################################################
    maxShow = 0
    for g in range(0, len(showList)):
        if (votes[g] > maxShow):
            whoWon = showList[g]
            maxShow = votes[g]
    return whoWon
def main():

    # initialize shows and votes lists, and choice variable
    shows  = ["Daredevil", "Fargo", 
              "Limitless", "Elementary", "Brooklyn 99", 
              "Empire", "Supergirl"]
    votes  = [0]*len(shows)
    choice = 1

    # print the voting number and show name
    for i in range(len(shows)):
        print(i + 1, "-", shows[i])
    # print the program greeting/instructions
    print("You and your friends are voting on a show to watch.")
    print("Which show would you like to vote for?")

    while choice != STOP:
        ######################################################
        # your code to call the function getVote() goes here #
        ######################################################
        # don't forget to handle the function's return value #
        ######################################################
        returnedVote = getVote(votes)
        
        if ((returnedVote <= 7) and (returnedVote >= 0)):
            if (returnedVote == 0):
                choice -= 1
            else:
                votes[returnedVote - 1] += 1
        else:
            print("Invalid vote -- try again")

    # once done voting, print the results
    print("\nHere are the final votes:")
    for i in range(len(shows)):
        print(shows[i], "has\t", votes[i], "votes")
    ########################################################
    # your code to call the function getWinner() goes here #
    ########################################################
    winner = getWinner(shows, votes)
    print(winner, "wins!")

main()


