#File: tv_shows.py
#Author: Austin Bailey
#Date: 3/22/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Program will help people decide what tv to watch.
def voteSystem(listOfShows):
    print("You and your friends are voting on a show to watch.")
    print("Which show would you like to vote for?")
    check = 1
    voteList = [0] * len(listOfShows)
    while (check != 0):
        vote = int(input("Enter '0' to stop voting: "))
        if ((vote <= 7) or (vote >= 0)):
            if (vote == 0):
                check -= 1
            else:
                voteList[vote - 1] += 1
        else:
            check = 1
    return voteList
def main():
    shows = ["Daredevil", "Fargo", "Limitless", "Elementary", "Brooklyn 99", "Empire", "Supergirl"]
    lengthOfList = len(shows)
    count = 1
    for g in range(0, lengthOfList):
        print(count, "-", shows[g])
        count += 1
    amountOfVotes = voteSystem(shows)
    print("Here are the final votes: ")
    for h in range(0, lengthOfList):
        print(shows[h], "has", amountOfVotes[h], "votes.")
main()
    
