#!/usr/bin/python3

# Author:           Martin Solum
# Date:             01NOV2024Fri
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 7 Lab
# Description:
"""
Theater Seating Lab:

A dramatic theater has three seating sections, and it charges the following prices for tickets in each section: section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each. The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. Design a program that asks for the number of tickets sold in each section and then displays the amount of income generated from ticket sales. The program should validate the numbers that are entered for each section.

i.e.
# asks for the number of tickets sold in each section.
# and then displays the amount of income generated from ticket sales.
# The program should validate the numbers that are entered for each section.
"""

import sys

# add the configure arg to go into configuration mode...
# i.e. to add, delete, or configure a section.
CONFIGURE = "configure"

sectionA = { "name":"A", "seats": 300, "price": 20.0, "seatsSold": 0 }
sectionB = { "name":"B", "seats": 500, "price": 15.0, "seatsSold": 0 }
sectionC = { "name":"C", "seats": 200, "price": 10.0, "seatsSold": 0 }

sectionsList = [ sectionA, sectionB, sectionC ]

def syntax():
    print( "\nsyntax:" )
    print( "to sell tickets enter the following with no arguments..." )
    print( "cis129_MartinSolum_Module7Lab_TheaterSeatingLab.py\n" )
    print( "to configure the system do the same but also pass the argument \"configure\"." )
    print( "e.g." )
    print( "cis129_MartinSolum_Module7Lab_TheaterSeatingLab.py configure" )

def money( amt ):
    return '${:,.2f}'.format( amt )

def getFloat( msg ):
    while True:
        try:
            userFloat = float(input( msg ))
            return userFloat
        except ValueError:
            print( 'ERROR: Invalid input, please enter a float!')

def getInteger( msg, lowLimit, highLimit ):
    while True:
        try:
            userInput = int( input( msg ))

            if not ( userInput >= lowLimit and userInput <= highLimit  ):
                raise AssertionError("AssertionError")
            
            return userInput

        except ValueError:
            print( 'ERROR: Invalid input, please enter a whole number!')

        except AssertionError:
            errorMsg = "Accepted values must be between " + str(lowLimit) 
            errorMsg = errorMsg + " & " + str(highLimit) + " Try again."
            print( errorMsg )

        continue

def printPricesTable():
    print(f'{"section name": ^20}{"price/seat": ^10}{"available": ^20}')
    for section in sectionsList:
        availableSeats = section["seats"] - section["seatsSold"]
        print(f'{section["name"]: ^20}{money(section["price"]): ^10}{availableSeats: ^20}')

# Give a subtotal for all purchases so far after each new purchase
def printSummaryTable():
    print(f'{"section name": ^20}{"price/seat": ^10}{"sold": ^10}{"revenue": ^20}')
    for section in sectionsList:
        revenue = section["seatsSold"] * section["price"]
        availableSeats = section["seats"] - section["seatsSold"]
        print(f'{section["name"]: ^20}{money(section["price"]): ^10}{section["seatsSold"]: ^10}{money(revenue): ^20}')

def displayWelcome():
    print( "Welcome! here are the section prices and seat availability." )
    printPricesTable()

def isValidSection( listOfKeyValues, keyName, value ):
    for record in listOfKeyValues:
        if record[ keyName ] == value:
            return True
    return False

def getRecord( listOfKeyValues, keyName, key ):
    for record in listOfKeyValues:
        if record[keyName] == key:
            return record

def getTotalSales():
    totalSales = 0
    for section in sectionsList:
        sectionSales = section["seatsSold"] * section["price"]
        totalSales += sectionSales
    return totalSales

def processPurchase():
    print( "processing purchase" )
    sectionName = ""
    while True:
        sectionName = str( input( "From which section will you be purchasing seats? " ))
        if isValidSection( sectionsList, "name", sectionName ):
            break
        else:
            print( "Bad section name, please try again." )
    
    section = getRecord( sectionsList, "name", sectionName )
    price = section["price"]

#    price = getTargetValue( sectionsList, "name", sectionName, "price" )
    print( "Excellent, section " + sectionName + " tickets cost " + money(price) + " each." )
    availableSeats = section["seats"] - section["seatsSold"]
    ticketsPurchased = getInteger( "how many tickets would you like to purchase? ", 0, availableSeats )
    print( "Great & thank-you. " )
    thisPurchase = ticketsPurchased * section["price"]
    print( str(ticketsPurchased)  + " tickets at " + money(section["price"]) + " comes to " + money(thisPurchase) )
    section["seatsSold"] += ticketsPurchased

def switch(command):
    if command == "add":
        name = str( input( "enter name of the new section: (e.g. D) " ))
        seats = getInteger( "enter number of seats in the new section: ", 0, 10000 )
        price = getFloat( "enter the price for a seat in the new section: " ) 
        newSection = { "name": name, "seats": seats, "price": price, "seatsSold": 0 }
        sectionsList.append( newSection )

    elif command == "delete":
        sectionName = str(input( "what is the name of the section to delete? " ))
        print( "you deleted", targetName )
        for section in sectionsList:
            if section["name"] == sectionName:
                sectionsList.remove( section )

    elif command == "edit":
        sectionName = str(input( "what is the name of the section to configure? " ))
        section = getRecord( sectionsList, "name", sectionName )
        seats = getInteger( "enter number of seats in the new section: ", 0, 10000 )
        section["seats"] = seats
        price = getFloat( "enter the price for a seat in the new section: " ) 
        section["price"] = price

    elif command == "return":
        print( "ok, let's make some sales!" )

def configureSections():
    command = None
    print( "Hello, you have activated the configuration system." )
    print( "with this interface you can add, delete, or edit seating sections." )
    while command != "return":
        command = str( input( "Please enter \"add\", \"delete\", \"edit\", or \"return\" " )).lower()
        switch( command )

def sellTickets():

    totalSales = 0

    while True:
        
        displayWelcome()

        processPurchase()

        printSummaryTable()
        
        flag = str( input( "Hello, would you like to record another purchase? (y/n) " ))
        
        if flag != "y":
            break

    print( "\nOk, heres the final breakdown:" )
    printSummaryTable()
    print( "total sales for today were: " + money(getTotalSales()) )
    print()

argCnt = len(sys.argv) - 1

if ( argCnt == 1 and sys.argv[1] == CONFIGURE ):
    configureSections()
    sellTickets()
elif argCnt == 0:
    sellTickets()
else:
    syntax()
    sys.exit(-1)
