#!/usr/bin/python3

# Author:           Martin Solum
# Date:             01OCT2024Tue
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 4 Lab ~ Decisions and Boolean Logic.
# Description:   

"""
The company wants a program to modify their bonus portion to include different levels and types and eliminate the day off program.  The program description is as follows:

A retail company assigns a $6,000 store bonus if monthly sales are more than $110,000; else if monthly sales are greater than or equal to $100,000 the store bonus is $5,000, else if monthly sales are greater than or equal to $90,000 the store bonus is $4,000, else if monthly sales are greater than or equal to $80,000, the store bonus is $3,000 otherwise a $0 amount or no store bonus is awarded.  They are using a percent of sales increase to determine if employees get individual bonuses.  If sales increased by an amount greater than or equal to 5% (0.05) then all employees get $75, else if sales increased by an amount greater than or equal to 4%, employees get $50, else if sales increased by an amount greater than or equal to 3% employees get $40 otherwise they get $0. 
"""

def money( amt ):
    return '${:,.2f}'.format( amt )
    
# ~ Step 1:  To accommodate the changes to the program, create the additional variables needed...

# Store bonus is a tiered schedule relative to monthly store sales...

storeAlphaThreshold = 110000.00
storeAlphaBonus = 6000.00

storeBetaThreshold = 100000.00
storeBetaBonus = 5000.00 

storeGammaThreshold = 90000.00
storeGammaBonus = 4000.00

storeDeltaThreshold = 80000.00
storeDeltaBonus = 3000.00

storeDefaultBonus = 0.00

# employee bonus is a tiered schedule relative to percent of sales growth...

employeeDefaultBonus = 0.0

employeeAlphaThreshold = 0.05
employeeAlphaBonus = 75.00

employeeBetaThreshold = 0.04
employeeBetaBonus = 50.0

employeeGammaThreshold = 0.03
employeeGammaBonus = 40.00

# declare local variables
monthlySales = 0.00         # monthly sales amount
storeBonus = 0.00        # store bonus amount
employeeBonus = 0.00        # employee bonus amount
percentSalesIncrease = 0.00   # percent of sales increase

# ~ Step 2:  The first section in the program is to get the monthly Sales... 

# include code to get the monthly Sales
prompt = "Please enter month's sales amount: "
monthlySales = float( input( prompt ))

# ~ Step 3:  The next section in the program calculates the store bonus...

# include code to Calculate the Store Bonus
def calculateStoreBonus( monthlySales):
    if monthlySales >= storeAlphaThreshold:
        return storeAlphaBonus
    elif monthlySales >= storeBetaThreshold:
        return storeBetaBonus
    elif monthlySales >= storeGammaThreshold:
        return storeGammaBonus
    elif monthlySales >= storeDeltaThreshold:
        return storeDeltaBonus
    else:
        return storeDefaultBonus

# ~ Step 4:  The next section of code will ask the user to enter the percent of sales increase...
# include code to get the Increase in Sales
prompt = "Please enter percent of sales increase: "

# The following lines guarantee the increaseString has a decimal...
"""
increaseString = ""
while ( increaseString.find( '.' ) == -1):
    increaseString = input( prompt )
    rawPercentFigure = float( increaseString )
"""
rawPercentageFigure = float( input( prompt ))
percentSalesIncrease = rawPercentageFigure / 100


# ~ Step 5:  Write code that will determine individual bonuses...
def calculateEmployeeBonus( percentSalesIncrease):

    # This code determines the Employee Bonus.
    if percentSalesIncrease >= employeeAlphaThreshold:
        return employeeAlphaBonus
    elif percentSalesIncrease >= employeeBetaThreshold:
        return employeeBetaBonus
    elif percentSalesIncrease >= employeeGammaThreshold:
        return employeeGammaBonus
    else:
        return employeeDefaultBonus

# ~ Step 6:  Write code that will print the store bonus and the employee bonus amount... 
storeBonus = calculateStoreBonus( monthlySales )
employeeBonus = calculateEmployeeBonus( percentSalesIncrease )

# This code prints the bonus information
print("The store bonus amount is $", money( storeBonus ))
print("The employee bonus amount is $", money( employeeBonus ))
if ( storeBonus == storeAlphaBonus ) and ( employeeBonus == employeeAlphaBonus ):
    print( 'Congrats! You have reached the highest bonus amounts possible!' )

# end of program file.
