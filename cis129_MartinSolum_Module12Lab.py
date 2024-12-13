#!/usr/bin/python3

# Author:           Martin Solum
# Date:             13DEC2024Fri
# Course:           CIS129 Prog & Problem Solv I
# Instructor:       Brittany Griwzow
# Assignment:       Module 12 Lab
# Description:
"""
Lab - Module 12
Convert the pseudocode into Python. Please submit your CIS129_YourName_Lab12.py file to D2L.
    1. Pet Class
Design a class named Pet, which should have the following fields:
        name: The name field holds the name of a pet.
        type: The type field holds the type of animal that a pet is. Example values are "Dog", "Cat", and "Bird".
        age: The age field holds the pets age.
    2. The Pet class should also have the following methods:
        setName: The setName method stores a value in the name field.
        setType: The setType method stores a value in the type field.
        setAge: The setAge method stores a value in the age field.
        getName: The getName method returns the value of the name field.
        getType: The getType method returns the value of the type field.
        getAge: The getAge method returns the value of the age field.
    3. Once you have designed the class, design a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. This data should be stored in the object. Use the objects accessor methods to retrieve the pets name, type, and age and display this data on the screen.  The output should be similar to the picture below.
Sample Pseudocode:
"""


# class variable to hold a pet
class Pet:
    # Fields
    petName = ""
    petType = ""
    petAge = 0

    # Constructor
    def __init__( self, inputName, inputType, inputAge ):
        self.petName = inputName
        self.petType = inputType
        self.petAge = inputAge

# Mutators

    def setName( self, petName ):
        self.petName = petName

    def setType( self, petType ):
        self.petType = petType

    def setAge( self, petAge ):
        self.petAge = petAge


# Accessors

    def getName( self ):
        return self.petName

    def getType( self ):
        return self.petType

    def getAge( self ):
        return self.petAge


def doMain():
    print( 'hello' )
    # Declare input variables
    # Declare String inputName, String inputType, Integer inputAge

    # Declare Pet Animal
    # create a Pet object
    firstPet = Pet( "", "", 0 )

    # Get values for a pet...
    # set pet name
    petName = input( "enter your pet's name:\n" )
    Pet.setName( firstPet, petName )

    # set pet type
    petType = input( "enter the pet's type:\n" )
    Pet.setType( firstPet, petType )

    # set pet age
    petAge = int( input( "enter the pet's age:\n" ) )
    Pet.setAge( firstPet, petAge )

    # Show values for this pet...
    # Display The pet name is Pet.getType()
    print( 'Your pet name: ' + Pet.getName( firstPet ) )

    # Display The pet type is Pet.getType()
    print( 'Your pet type: ' + Pet.getType( firstPet ) )

    # Display The pet age is Pet.getAge()
    print( 'Your pet age: ' + str( Pet.getAge( firstPet ) ) )


# main module
if __name__ == '__main__':
    doMain()
