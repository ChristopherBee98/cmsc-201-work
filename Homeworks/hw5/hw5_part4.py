#File: hw5_part4.py
#Author: Austin Bailey
#Date: 3/5/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Compete for extra points.

def pointTaking(points, tracker):
    failSafe1 = 1
    failSafe2 = 1
    failSafe3 = 1
    if ((tracker % 2) == 0):
        if (points >= 3):
            while (failSafe1 == 1):
                pointsTaken = int(input("Player 2, how many points do you take? (1-3): "))
                if ((pointsTaken > 3) or (pointsTaken < 1)):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe1 += 1
        elif (points == 2):
            while (failSafe2 == 1):
                pointsTaken = int(input("Player 2, how many points do you take? (1-2): "))
                if ((pointsTaken > 2) or (pointsTaken < 1)):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe2 += 1
        elif (points == 1):
            while (failSafe3 == 1):
                pointsTaken = int(input("Player 2, how many points do you take? (1): "))
                if (pointsTaken != 1):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe3 += 1
    elif ((tracker % 2) == 1):
        if (points >= 3):
            while (failSafe1 == 1):
                pointsTaken = int(input("Player 1, how many points do you take? (1-3): "))
                if ((pointsTaken > 3) or (pointsTaken < 1)):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe1 += 1
        elif (points == 2):
            while (failSafe2 == 1):
                pointsTaken = int(input("Player 1, how many points do you take? (1-2): "))
                if ((pointsTaken > 2) or (pointsTaken < 1)):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe2 += 1
        elif (points == 1):
            while (failSafe3 == 1):
                pointsTaken = int(input("Player 1, how many points do you take? (1): "))
                if (pointsTaken != 1):
                    print("Bruh, put the correct amount of points in.")
                else:
                    failSafe3 += 1
    remainingPoints = points - pointsTaken
    return remainingPoints
def main():
    print("Welcome to the extra points game!")
    failSafe = 1
    while (failSafe == 1):
        totalPoints = int(input("Enter the number of points to play for (13-21): "))
        if ((totalPoints > 21) or (totalPoints < 13)):
            print("Error: please enter the correct amount of points.")
        else:
            failSafe += 1
    playerTracker = 1
    while (totalPoints != 0):
        playerTracker += 1
        if ((playerTracker % 2) == 0):
            print("Player 2 starts")
            print("There are", totalPoints, "points left.")
            totalPoints = pointTaking(totalPoints, playerTracker)
        elif ((playerTracker % 2) == 1):
            print("Player 1 starts")
            print("There are", totalPoints, "points left.")
            totalPoints = pointTaking(totalPoints, playerTracker)
    if ((playerTracker % 2) == 0):
        print("Congratulations! Player 2 has won!")
    elif ((playerTracker % 2) == 1):
        print("Congratulations! Player 1 has won!")
main()
