#!/usr/bin/python3

# Author:           Martin Solum
# Date:             26NOV2024Tue
# Course:           CIS129 Prog & Problem Solv I
# Instructor:       Brittany Griwzow
# Assignment:       Module 10 Lab
# Exercise:         Dietel & Dietel Exercise 8.1
# Description:
"""
8.1 ( CHECK PROTECTION ) Although electronic deposit has become extremely popular, payroll and accounts payable applications often print checks. A serious problem is the intentional alteration of a check amount by someone who plans to cash a check fraudulently. To prevent a dollar amount from being altered, some computerized check-writing systems employ a technique called check protection. Checks designed for printing by computer typically contain a fixed number of spaces for the printed amount. Suppose a paycheck contains eight blank spaces in which the computer is supposed to print the amount of a weekly paycheck. If the amount is large, then all eight of the spaces will be filled:

1,230.60 ( check amount )
--------
01234567 ( position numbers )
On the other hand, if the amount is smaller, then several of the spaces would ordinarily be left blank. For example,

  399.87
--------
01234567

contains two blank spaces. If a check is printed with blank spaces, it's easier for someone to alter the amount. Check-writing systems often insert leading asterisks to prevent alteration and protect the amount as follows:

**399.87
--------
01234567

Write a script that inputs a dollar amount, then prints the amount in check-protected format in a field of 10 characters with leading asterisks if necessary. [Hint: In a format string that explicitly specifies alignment with <, ^ or >, you can precede the alignment specifier with the fill character of your choice.]
"""
def errorMessages():
    print( 'This program only accepts floats.' )
    print( 'The float entered must be under 10 chars long.' )
    print( 'The presentation format is \'$$$,$$$.dd\'.' )
    print( 'The highest allowable number is 999999.99.' )
    print( 'The user must manually enter the decimal point.' )
    print( 'The user must manually enter tenths & hundredths places, even for 0.00.' )
    print( 'The user does not enter the commas.  The system will do that automatically.' )
    print( 'please re-attempt to enter your floating point number.' )

def getFloat( message ):
    while True:
        try:
            strTester = input( message )
            userInput = float( strTester )
            #userInput = float( input( message ) )
            #strTester = str( userInput )
            
            # note: the field must have no more than 10 chars.
            if len( strTester ) > 10:
                print( strTester )
                print( '0123456789' )
                raise AssertionError('AssertionError')

            if strTester[-3:-2] != '.':
                raise AssertionError('AssertionError')

            if ( userInput < 0 or userInput >= 1000000.00 ):
                raise AssertionError()

            return userInput

        except ValueError:
            errorMessages()

        except AssertionError:
            errorMessages()

# get the user's floating point number.
fpn = getFloat( 'please enter a floating point number:\n' )

# Print right justified and left filled with asterisks.
print( f'{fpn:*>10,.2f}' )
print( '0123456789' )

