#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#

def reverseStr(word):
    word = word[::-1]
    return word

def containsWord(containingStr,containedStr):
    if containedStr in containingStr:
	    return "Yes"
    else:
	    return "No"

def isPalindrome(word):
    if word == reverseStr(word):
	    return "Yes"
    else:
	    return "No"

def upperCaseStr(word):
    return word.upper()

