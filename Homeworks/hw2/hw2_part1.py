#File: hw2_part1.py
#Author: Austin Bailey
#Date: 2/12/2016
#Lab Section: 10
#UMBC email: baustin1@umbc.edu
#Description: This program answers the questions one through ten.

#Question 1
#Expected Output: 55
num1 = (7 + 4) * 5
print("Question 1: ", num1)
#Actual Output: 55
#Explanation: 7 and 4 are added together first in the parenthesis, and the number 11 is then multiplied by 5. This gives us 55.

#Question 2
#Expected Output: 1
num2 = (15 % 7)
print("Question 2: ", num2)
#Actual Output: 1
#Explanation: When dividing 15 by 7, you can only get up to 2 before not being able to divide anymore. The remaining value is then 1, which is the answer.

#Question 3
#Expected Output: 0
num3 = (32 % 36)
print("Question 3: ", num3)
#Actual Output: 32
#Explanation: Because 36 is larger than 32, it cannot be divided even once. As a result, it defaults to 32.

#Question 4
#Expected Output: 12
num4 = (5 - 3) + (10 - 5) * (8 % 3)
print("Question 4: ", num4)
#Actual Output: 12
#Explanation: Parenthesis come first, which results in the equation 2 + 5 * 2. Multiplication comes before addition, which means 2 + 10. This equals 12.

#Question 5
#Expected Output: 4.5
num5 = 21 / 7 / 4 * (3 + 3)
print("Question 5: ", num5)
#Actual Output: 4.5
#Explanation: Parenthesis come first. After that, the equation goes from left to right since division and multiplication have the same priority. This results in the number 4.5.

#Question 6
#Expected Output: 14
num6 = 9 / 3 + 21 - 5 * 2
print("Question 6: ", num6)
#Actual Output: 14
#Explanation: Division and multiplication come first. After that, we're left with 3 + 21 - 10. We go from left to right at this point to get the number 14.

#Question 7
#Expected Output: 14
num7 = 7 % 5 + 6 * 2
print("Question 7: ", num7)
#Actual Output: 14
#Explanation: Modulus and multiplication have higher priority then addition. Therefore, the equation is 2 + 12. We add, and get 14.

#Question 8
#Expected Output: 17.3
num8 = 35.2 / 2.3 + (332 % 33)
print("Question 8: ", num8)
#Actual Output: ~17.3
#Explanation: Parenthesis and division both have higher priority over addition. Therefore, 35.2 divided by 2.3 is roughly 15.3 and 332 modulus 33 is 2. Adding those two numbers results in 17.3.

#Question 9
num9 = 55 / (10 + 45) / 0.2
target9 = 5.0
print("Question 9: ", num9, target9)

#Question 10
num10 = 65 // (20 + 10) - 4 % 4
target10 = 2
print("Question 10: ", num10, target10)
