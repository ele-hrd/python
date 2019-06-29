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
given_string = input("<<< ")
substring = input("which substring you want to find ? ")
def countOccur(given_string,substring):
    return given_string.count(substring)
print("Total",countOccur(given_string,substring))

#4)count the total no of occurence of substring in given string (without using count method)
given_string = input("<<< ")
converted_list = given_string.split(" ")
substring = input("which substring you want to find ? ")
def countOccur(converted_list,substring):
    counter = 0
    for word in converted_list:
        if word.lower() == substring.lower():
            counter += 1
    return counter
print("Total :",countOccur(converted_list,substring))            


#5)
converted_list = ''
substring = ''
def countOccur(converted_list = None,substring = None):
    given_string = input("<<< ")
    converted_list = given_string.split(" ")
    substring = input("which substring you want to find ? ")
    counter = 0
    for word in converted_list:
        if word.lower() == substring.lower():
            counter += 1
    if counter == 0:
        print("Sorry !!! we didn't find your match...")
    return counter
print("Total :",countOccur(converted_list,substring))
asking  = input("Do you still wanna try it ?[yes/no] ")
for i in range(0,100):
    if asking.lower() == "yes":
        print("Total :",countOccur(converted_list,substring))
        break
    elif asking.lower() == "no":
        break
    else:
        print("Please write either yes or no...")            
        asking  = input("Do you still wanna try it ?[yes/no] ")
print("Thanks for your time...") 

#6)finding the position of substring in any given string 
#7)finding the position of substring in any given string (without using find method)
      

