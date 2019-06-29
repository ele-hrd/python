# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:27:06 2019

@author: Hardik
"""
#Methods of string
#1)add 50 character  space before any given string
given_string = input(">>> ")
converted_string = given_string.center(50)
print(converted_string)

#2)add 50 character  space before any given string
given_string = input(">>> ")
converted_string = given_string.center(50,"&")
print(converted_string)

#3)count the total no of occurence of substring in given string
given_string = input("<<<")
substring = input("which substring you want to find ? ")
def countOccur(given_string,substring):
    return given_string.count(substring)
print("Total",countOccur(given_string,substring))
