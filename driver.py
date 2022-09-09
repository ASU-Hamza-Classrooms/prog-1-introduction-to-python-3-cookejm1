#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print("\t" + "Input string is " + inputStr)
    print("\t"+"Reverse of string is "+reverseStr(inputStr))
    print("\t" + "Does string contain apple? " + containsWord(inputStr,"apple"))
    print("\t" + "Does string contain banana? " + containsWord(inputStr,"banana"))
    print("\t" + "Is string a palindrome? " + isPalindrome(inputStr))
    print("\t" + "Uppercase of string is " + upperCaseStr(inputStr))
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    obj = Worker(inputStr)
    print("\t" + "Input string is " + inputStr)
    print("\t" + "Reverse of string is "+ obj.reverseStr())
    print("\t" + "Does string contain apple? " + obj.containsWord("apple"))
    print("\t" + "Does string contain banana? " + obj.containsWord("banana"))
    print("\t" + "Is string a palindrome? " + obj.isPalindrome())
    print("\t" + "Uppercase of string is " + obj.upperCaseStr())
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




