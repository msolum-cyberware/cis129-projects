#!/usr/bin/python3

# Author:           Martin Solum
# Date:             11OCT2024Fri
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 5 lab.
# Exercise:         <if required>
# Description:   

from decimal import Decimal

"""
Write a program that will allow a grocery store to keep track of the total number of bottles collected for seven days.

The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times .10 cents).

The output of the program should include the total number of bottles returned and the total paid out.

The program will ask the user if they have more data to enter and will end the program if they do not.
"""

# variables...

payoutPerBottle = Decimal( str('.10') )

totalBottles = 0    # accumulated bottle values.
counter = 1         # loop control counter.
todayBottles = 0    # number of bottles returned on a day.
totalPayout = 0     # calculated value of totalBottles times .10.
keepGoing = "y"     # continue running program flag.

def getProcessAWeeksDate ( totalBottles, totalPayout):
    todayBottles = int( input( "Enter number of bottles for day #" + str( counter ) + ": " ))
    totalBottles += todayBottles

    # code to set value of variable totalPayout
    totalPayout = totalBottles * payoutPerBottle
    return totalBottles, totalPayout

while keepGoing == "y":

    # code to set value of variable totalBottles
    totalBottles = 0
    todayBottles = 0
    counter = 1

    while counter <= 7:
        totalBottles, totalPayout = getProcessAWeeksDate( totalBottles, todayBottles )
        counter += 1        
        # end of inner while

    # code to print the number of total bottles and total payout
    print( 'The total number of bottles collected is ' + str( totalBottles ))
    print( f'The total paid out is $ {totalPayout:>5.2f}')
    keepGoing = input( "Do you want to enter another week?\n(Enter y or n): " )

# end of outer while...
