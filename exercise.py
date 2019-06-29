# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1)first character lowercase
old_string = "Good Morning"
new_string = old_string[0].lower() + old_string[1:]
print(new_string)

#2)first character uppercase
old_string  = "good morning"
new_string = old_string[0].upper() + old_string[1:]
print(new_string)

#3)first character of second word lowercase
old_string = "Good Morning"
old_list = old_string.split(" ")
new_string = old_list[0]  + " " + old_list[1].lower()
print(new_string)

#4)replace commas with dots in 
old_string = "14,2,4,5,6"
new_string = old_string.replace(",",".")
print(new_string)

#method 2) using marketrans and translate
old_string = "a,c,d,f,g,d"
new_string = old_string.maketrans(',','.')
print(old_string.translate(new_string))

#5)rotate string by 3 character from its default position to right side
#e.g. input -> "Morning"
#     output -> "ingmorn"
old_string = "Morning"
last_string_part = old_string[:-3]
first_string_part = old_string[4:]
print(first_string_part + last_string_part)

#6 rotate input string by n character from its default position to right side
old_string = input(">>> ")
n = int(input("Enter the number you wanted to rotate: "))
last_part_string = old_string[:-n]
first_part_string = old_string[n+1:]
print(first_part_string + last_part_string)

#7)rotate string by 3 character from its default position to left side
#e.g. input -> "Morning"
#     output -> "ningMor"
n = 3
old_string = "Morning"
total_character = len(old_string)
first_string = old_string[n:]
last_string = old_string[0:total_character-n]
print(first_string + last_string)

#8) rotate input string by n character from its default position to left side
old_string = input(">>> ")
n = int(input("Enter the number you wanted to rotate: "))
total_character = len(old_string)
first_string = old_string[n:]
last_string = old_string[0:total_character-n]
print(first_string + last_string)

