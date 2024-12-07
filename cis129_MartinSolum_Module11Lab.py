#!/usr/bin/python3

# Author:           Martin Solum
# Date:             06DEC2024Fri
# Course:           CIS129 Prog & Problem Solv I
# Instructor:       Brittany Griwzow
# Assignment:       Module 11 <?> <assignment type>
# Exercise:         <if required>
# Description:
"""
there are 2 argument array scenarios.

cis129_MartinSolum_Module10Lab.py -w <dataFilename>.txt
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.txt

the -w option...
the -w option instructs the program to write new data to create a new data file.

the -r option...
the -r option instructs the program to read an existing data file and present the data. 

important caveat: at this time the program only recognizes two file types, .txt & .csv.
The user signals the filetype withthe file suffix so proper file naming is imperative.

so these calls are legal...
cis129_MartinSolum_Module10Lab.py -w <dataFilename>.txt
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.txt
cis129_MartinSolum_Module10Lab.py -w <dataFilename>.csv
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.csv

but these calls are CURRENTLY not allowed...
cis129_MartinSolum_Module10Lab.py -w <dataFilename>.json
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.json
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.odt
cis129_MartinSolum_Module10Lab.py -r <dataFilename>.odt

"""
import sys
import csv
import pandas as pd

#*******************************************************************************
#*******************************************************************************
#***                                                                         ***
#*** Read & Write functions...                                               ***
#***                                                                         ***
#*******************************************************************************
#*******************************************************************************

def getDataAsString():
    firstName = inputString( 'Input firstName:\n' )
    lastName = inputString( 'Input lastName:\n' )
    score1 = inputNumber( 'Input first test score:\n' )
    score2 = inputNumber( 'Input second test score:\n' )
    score3 = inputNumber( 'Input third test score:\n' )
    record = firstName + ' ' + lastName + ' ' + str( score1 )
    record += ' ' + str( score2 ) + ' ' + str( score3 ) + '\n'
    return record


def writeTxt( filename ):
    print( "write txt file." )
    goFlag = True
    with open( filename, mode='w') as students:

        while goFlag == True:
            record = getDataAsString()
            students.write( record )
            if input( 'Another record?(y/n)' ) != 'y':
                goFlag = False

def readTxt( filename ):
    print( "read txt file." )
    with open( filename, mode='r') as students:
        labels = f'{"Last name":<15}{"First Name":<15}{"Score #1":^12}{"Score #2":^12}'
        labels = labels + f'{"Score #3":^12}{"total":^12}{"count":^12}{"average":^12}'
        print( labels )
        for record in students:
            lastName, firstName, score1, score2, score3 = record.split()
            scores = pd.Series( [int(score1), int(score2), int(score3)] )
            total = scores.sum()
            count = scores.count()
            average = scores.mean()
            str = f'{lastName:<15}{firstName:<15}{score1:^12}{score2:^12}{score3:^12}'
            str = str + f'{total:^12}{count:^12}{average:^12,.2f}'
            print( str )


def writeCSV( filename ):
    print( "write csv file." )
    goFlag = True
    with open( filename, mode='w', newline='' ) as students:
        writer = csv.writer( students )

        while goFlag == True:
            record = getDataAsString()
            recordAsList = record.split()
            writer.writerow( recordAsList )
            if input( 'Another record?(y/n)' ) != 'y':
                goFlag = False

def readCSV( filename ):
    print( "read csv file." )
    with open( filename, 'r', newline='' ) as students:
        labels = f'{"Last name":<15}{"First Name":<15}{"Score #1":^12}{"Score #2":^12}'
        labels = labels + f'{"Score #3":^12}{"total":^12}{"count":^12}{"average":^12}'
        print( labels )
        reader = csv.reader( students )
        for record in reader:
            lastName, firstName, score1, score2, score3 = record
            scores = pd.Series( [int( score1 ), int( score2 ), int( score3 )] )
            total = scores.sum()
            count = scores.count()
            average = scores.mean()
            str = f'{lastName:<15}{firstName:<15}{score1:^12}{score2:^12}{score3:^12}'
            str = str + f'{total:^12}{count:^12}{average:^12,.2f}'
            print( str )


#*******************************************************************************
#*******************************************************************************
#***                                                                         ***
#*** MAIN CODE SECTION...                                                    ***
#***                                                                         ***
#*******************************************************************************
#*******************************************************************************


def doMain( args ):
    # print( "The argument is ~> " + args[1] + ' ' + args[2] )
    verbParm = sys.argv[1]
    checkVerb( verbParm )

    filename = sys.argv[2]
    checkSuffix( filename )
    suffix = getSuffix( filename )

    if ( verbParm == '-w' and suffix=='.txt' ):
        writeTxt( filename )
    elif ( verbParm == '-r' and suffix=='.txt' ):
        readTxt( filename )
    elif ( verbParm == '-w' and suffix=='.csv' ):
        writeCSV( filename )
    elif ( verbParm == '-r' and suffix=='.csv' ):
        readCSV( filename )


#*******************************************************************************
#*******************************************************************************
#***                                                                         ***
#*** DATA VALIDATION SECTION...                                              ***
#***                                                                         ***
#*******************************************************************************
#*******************************************************************************


def inputNumber( message ):
    BOTTOM = 0
    TOP = 100

    while True:

        try:
            userInput = int( input( message ) )
            if not ( BOTTOM <= userInput and userInput <= TOP ):
                raise AssertionError( "integer out of range." )

        except ValueError:
            print( "Not an integer! Try again." )
            continue

        except AssertionError:
            print( "oops, number must be such that " + str( BOTTOM ) +
                  " <= number <= " + str( TOP ) )
            continue

        else:
            return userInput


def inputString( message ):

    while True:
        try:
            userInput = str( input( message ) )
            if not ( 1 <= len( userInput ) and len( userInput ) <= 15 ):
                raise AssertionError( "bad string length." )

        except AssertionError:
            print( "string to short or long... " )
            continue

        except ValueError:
            print( "Not a string" )
            continue

        else:
            return userInput


#*******************************************************************************
#*******************************************************************************
#***                                                                         ***
#*** PARAMETER VALIDATION SECTION...                                         ***
#***                                                                         ***
#*******************************************************************************
#*******************************************************************************

def checkVerb( verbParm ):
    permittedVerbs = ['-r', '-w']
    if verbParm not in permittedVerbs:
        print( 'Bad VERB!' )
        syntax()
        sys.exit( -2 )

def getSuffix( filename ):
    return filename[filename.rfind( '.' ):]
    
def checkSuffix( filename ):
    if filename.rfind( '.' ) == -1:
        print( 'NO SUFFIX!' )
        syntax()
        sys.exit( -3 )
    permittedSuffixes = ['.txt', '.csv']
    suffix = getSuffix( filename )
    if suffix not in permittedSuffixes:
        print( 'illegal suffix: ' + suffix )
        syntax()
        sys.exit( -4 )


#*******************************************************************************
#*******************************************************************************
#***                                                                         ***
#*** PARAMETER DECISION SECTION...                                           ***
#***                                                                         ***
#*******************************************************************************
#*******************************************************************************


def syntax():
    print( "\nsyntax:" )
    print( "\trunner [ -r or -f ] [yourDataFilename.fileSuffix]" )
    print( "\t\te.g." )
    print( "\trunner -w  [yourDataFilename].txt" )
    print( "\trunner -r  [yourDataFilename].txt" )
    print( "\trunner -w  [yourDataFilename].csv" )
    print( "\trunner -r  [yourDataFilename].csv" )


argCnt = len( sys.argv ) - 1

if ( argCnt != 2 ):
    print( argCnt )
    syntax()
    sys.exit( -1 )

if __name__ == '__main__':
    doMain( sys.argv )
