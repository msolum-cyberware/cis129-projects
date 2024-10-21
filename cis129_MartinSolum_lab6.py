#!/usr/bin/python3

# Author:           Martin Solum
# Date:             22OCT2024Tue
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 6 lab
# Description:   

"""
Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
"""

# Converted the Pseudocode code to Python Code and saved as Lab6.py
import math

# main module                                 
def main():
   # Local variable for the total number of hot dogs needed.
   total =  0

   # Input --------------------------------------
   # Get the total number of hot dogs needed.
   total = getTotalHotDogs()

   # Processing ----------------------------------
   # Named constants for the package sizes
   DOGS = 10   # Hot dogs in a package
   BUNS = 8    # Hot dog buns in a package

   # Local variables
   dogsLeft = 0  # Left over hot dogs
   bunsLeft = 0  # Left over hot dog buns
   minDogs = 0   # Minimum packages of hot dogs
   minBuns = 0   # Minimum packages of hot dog buns

   # Calculate the number of left over hot dogs.
   dogsLeft = (DOGS - total % DOGS) % DOGS

   # Calculate the minimum number of packages of hot dogs.
   minDogs = math.ceil(total / DOGS) 

   # Calculate the number of left over hot dog buns.
   bunsLeft = (BUNS - total % BUNS) % BUNS

   # Calculate the minimum number of packages of hot dogs buns.
   minBuns = math.ceil(total / BUNS) 

   # Output ----------------------------------------
   # Display the results.
   showResults(dogsLeft, minDogs, bunsLeft, minBuns)

# The getTotalHotDogs module gets the number of people
# attending the cookout and the number of hot dogs each
# person will be given, and stores the product in the
# totalHotDogs reference variable.

def getTotalHotDogs():

   # Local variables
   people = 0  # Number of people attending
   hotDogs = 0  # Hot dogs per person

   # Get the number of people attending the cookout.
   people = int( input( "Enter the number of people attending the cookout: " ))

   # Get the number of hot dogs each person will be given.
   hotDogs = int( input( "Enter the number of hot dogs for each person: " ))

   # Calculate the total number of hot dogs needed.
   total = people * hotDogs
   return total

# The showResults module accepts the total number of hot dogs
# as an argument and calculates the minimum packages of hot
# dogs and hot dog buns, the left over hot dogs and hot dog
# buns, and displays the results.

def showResults( dogsLeft, minDogs, bunsLeft, minBuns ):

   # Display the minimum packages of hot dogs needed.
   print( "Minimum packages of hot dogs needed: ", minDogs )

   # Display the minimum packages of buns needed.
   print( "Minimum packages of hot dog buns needed: ", minBuns )

   # Display the number of hot dogs left over.
   print( "Hot dogs left over: ", dogsLeft )

   # Display the number of hot dog buns left over.
   print( "Hot dog buns left over: ", bunsLeft )


main()
