#!/usr/bin/python3

# Author:           Martin Solum
# Date:             22NOV2024
# Course:           CIS129 Prog & Problem Solv I
# Instructor:       Brittany Griwzow
# Assignment:       Module 09 Extra Credit
# Description:   

""" 
The extra credit assignment was to finish the program we did in class 20DEC2024.  
That program elicited users names and their birthdays.
It then summarized the collected data.

I modified the program to do input validation on the birthday.
I verified that the date given is actually a real date.
I request that the user uses the ddMMMyyyy date format that I like.
However, the string format is a variable so any desired standard date form could be used.
"""

import sys
from datetime import datetime

formatStr = '%d%b%Y'

# a function to check if the date data is valid...
def checkDate( dateStr ):

    try:
        datetime.strptime( dateStr, formatStr )
        return True

    except ValueError:
        return False

# a function for getting date data....
def getValidDate():
    
    goodDate = False
    userDate = ''

    while( not goodDate ):
        userDate = input( 'Please enter your birthday in \'' + formatStr + '\' format.\n' )
        goodDate = checkDate( userDate )

    return userDate


# birthday demo based on "Automate the Boring Stuff" page 133...
birthDays = {}
done = False

while ( not done ):
    
    name = input( 'NAME: (blank to quit)\n' )

    if name == '':
        done = True

    elif name in birthDays.keys():
        print( name + "'s birthday is " + birthDays[name] )

    else:
        print( "Birthday?" )
        bday = getValidDate()
        print( bday )
        birthDays.update( { name:bday } )
    
# after data is entered, print data summary.
for k,v in birthDays.items():
    print( k + "'s birthday is " + v )
