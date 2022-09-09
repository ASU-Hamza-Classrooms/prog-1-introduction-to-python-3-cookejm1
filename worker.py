#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
#
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
#
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

class Worker:

    def __init__(self,str):
	    self.str = str

    def reverseStr(self):
	    return self.str[::-1]

    def containsWord(self,containedStr):
	    if self.str in containedStr:
		    return "Yes"
	    else:
		    return "No"

    def isPalindrome(self):
	    if self.str == reverseStr(self.str):
		    return "Yes"
	    else:
		    return  "No"

    def upperCaseStr(self):
	    return self.str.upper()


