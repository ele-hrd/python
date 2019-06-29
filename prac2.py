# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 02:02:32 2019

@author: Hardik
"""

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