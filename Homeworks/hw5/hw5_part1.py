#File: hw5_part1.py
#Author: Austin Bailey
#Date: 3/4/2016
#Section: 10
#E-mail: baustin1@umbc.edu
#Description: Calculates a tip at a given restaurant.

def levelOfService(finalBill, quality):
    if (quality == 'excellent'):
        tip = finalBill * .25
        return tip
    elif (quality == 'good'):
        tip = finalBill * .2
        return tip
    elif (quality == 'bad'):
        tip = finalBill * .1
        return tip
def main():
    x = 1
    totalBill = float(input("What is the total bill? "))
    while (x == 1):
        print("What was the quality of service?")
        serviceQuality = str(input("Say excellent, good, or bad: "))
        if (serviceQuality == ('excellent' or 'good' or 'bad')):
            x += 1
        serviceTip = levelOfService(totalBill, serviceQuality)
    totalAmount = serviceTip + totalBill
    print("The bill was $"+str(totalBill))
    print("The service was",serviceQuality)
    print("The tip is $"+str(serviceTip))
    print("The grand total with tip is $"+str(totalAmount))
main()
