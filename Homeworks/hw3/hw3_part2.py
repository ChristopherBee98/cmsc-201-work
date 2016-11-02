#File: hw3_part2.py
#Author: Austin Bailey
#Date: 2/20/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program will calculate a grade.

def main():
    homeworkWeight = float(input("Please enter the homework weight: "))
    homeworkGrade = int(input("Please enter the homework grade: "))
    examWeight = float(input("Please enter the exam weight: "))
    examGrade = int(input("Please enter the exam grade: "))
    discussionWeight = float(input("Please enter the discussion weight: "))
    discussionGrade = int(input("Please enter the discussion grade: "))
    totalHomework = homeworkWeight * homeworkGrade
    totalExam = examWeight * examGrade
    totalDiscussion = discussionWeight * discussionGrade
    totalGrade = totalExam + totalHomework + totalDiscussion
    print("The final numerical grade is:",totalGrade)
    if (totalGrade >= 90):
        print("This earns you an A in the class.")
    elif (90 > totalGrade >= 80):
        print("This earns you a B in the class.")
    elif (80 > totalGrade >= 70):
        print("This earns you a C in the class.")
    elif (70 > totalGrade >= 60):
        print("This earns you a D in the class.")
    else:
        print("This earns you an F in the class. You fail.")
main()
