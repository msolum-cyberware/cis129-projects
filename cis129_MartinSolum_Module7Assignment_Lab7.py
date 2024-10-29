#!/usr/bin/python3

# Author:           Martin Solum
# Date:             29OCT2024Tue
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 7 assignment lab
# Exercise:         lab 7-3 The Dice Game.
# Description:   

"""
each player gets a single roll of a 6 faced die.

The highest roll wins.

players continue to play until they answer 'no' to the continue to play prompt.
"""

# Lab 7-3 The Dice Game
# add libraries needed
import random

# the main function
def main():

    # initialize variables
    endProgram = 'no'
    playerOne = playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames( playerOne, playerTwo )

    # while loop to run program again
    while endProgram == 'no':

        # populate variables
        winnerName = 'NO NAME'
        p1number = p2number = 0

        # call to rollDice
        winnerName = rollDice( p1number, p2number, playerOne, playerTwo, winnerName )

        # call to displayInfo
        displayInfo( winnerName )

        endProgram = input('Do you want to end program? (yes/no): ')


#this function gets the players names
def inputNames( playerOne, playerTwo ):
    playerOne = input( 'Enter name of playerOne: ' )
    playerTwo = input( 'Enter name of playerTwo: ' )
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    print( playerOne + " rolled a ", p1number )

    p2number = random.randint(1, 6)
    print( playerTwo + " rolled a ", p2number )

    if ( p1number > p2number ):
        winnerName = playerOne
    elif ( p2number > p1number ):
        winnerName = playerTwo
    else:
        winnerName = "TIE"

    return winnerName

#this function displays the winner
def displayInfo( winnerName ):
    if ( winnerName == "TIE" ):
        print( "Congrats everyone! it was a TIE." )
    else:
        print( winnerName )

# calls main
main()

