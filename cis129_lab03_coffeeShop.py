#!/usr/bin/python3
# Author:       Martin Solum
# Date:         20SEP2024Fri
# Course:       CIS129
# Assignment:   Module 3 Lab.
# Description:  Query User order, calculate extensions & tax, & print receipt.

# ~ set price constants.
coffeeUnitPrice = 5
muffinUnitPrice = 4
taxRate = 6

def printStars():
    star = "*"
    line = ""
    for i in range(1,40):
        line = line + star
    print(line)

def printDashes():
    dash = "-"
    line = ""
    for i in range(1, 10):
        line = line + dash
        

def money( amt ):
    return '${:,.2f}'.format( amt )
        
# ~ INPUT: query customer data.

printStars()

print( "My Coffee and Muffin Shop" )

# query coffeeUnits.
coffeeUnits = int( input( "Number of coffees bought?\n" ))

# query muffinUnits.
muffinUnits = int( input( "Number of muffins bought?\n" ))

printStars()                  
print()
printStars()

# ~ PROCESSING: calculate extensions, subtotal, tax, total, etc.
coffeeExtension = coffeeUnits * coffeeUnitPrice
muffinExtension = muffinUnits * muffinUnitPrice
subtotal = coffeeExtension + muffinExtension
tax = taxRate / 100 * subtotal
total = subtotal + tax

# ~ OUTPUT: present receipt.
print( "My Coffee and Muffin Shop Receipt" )
print( str( coffeeUnits ) + " Coffee at $" + str( coffeeUnitPrice ) \
        + " each: " + money( coffeeExtension ))
print( str( muffinUnits ) + " Muffin at $" + str( muffinUnitPrice ) \
         + " each: " + money( muffinExtension ))
print( str( taxRate ) + "% tax: " + money( tax )) 
printDashes()
print( "Total: " + money( total ))
printStars()


"""                  
display coffeeDetails
display muffinDetails
display tax
display total
"""

