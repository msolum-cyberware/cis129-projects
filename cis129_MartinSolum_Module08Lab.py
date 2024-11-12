#!/usr/bin/python3
# Author:           Martin Solum
# Date:             12NOV2024Tue
# Course:           CIS129
# Instructor:       Brittany Griwzow
# Assignment:       Module 08 Lab
# Exercise:         Dietel & Dietel exercise 5.9
# Description:   

"""
A string that is spelled identically backward and forward, like 'radar', is a palindrome. Write a function is_palindrome that takes a string and returns True if it is as palindrome and False otherwise. Use a stack (simulated with a list as we did in Section 5.11) to help determine whether a string is a palindrome. Your function should ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation.

Submit completed Python code as a .py source file to D2L

*********************************************
examples of palindromes:
    noon
    radar
    Racecar
    Taco cat.
    Do geese see God?

"""

from math import floor

def loweredAndStripped( text ):
    text = text.lower()
    las = ""
    for ch in text:
        if ord(ch) >= 97 and ord(ch) <= 122:
            las += ch
    return las

def isPalindrome( text ):
    text = loweredAndStripped( text )
    length = len( text )
    middle = floor( length / 2 )

    for i in range( 0, middle ):
        coIndex = length -i -1
        if text[i] != text[coIndex]:
            return False
    return True

text = input( "Enter text:\n" )
print( text )
print( isPalindrome( text ))

