"""
File Name: firstifprogram.py
Creator: Ammon Jones
Purpose: Compare numbers & strings
"""
# Libraries needed to complete the task:

# Functions needed to complete the task:

# Constants needed to complete the task:
favorite_animal = 'Snow leoPard'

#Comparing ints program
# Info needed from user to complete the task:
print('Please enter the information below:')
int1 = int(input('Integer 1: '))
int2 = int(input('Integer 2: '))

#Comparing ints
if int1 > int2:
    print('The first number is greater')
else:
    print('The first number is not greater')    

if int1 == int2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if int1 < int2:
    print('The second number is greater')
else:
    print('The second number is not greater')

#Guessing favorite animal program:
#Info needed from user
user_animal = input('What is your favorite animal? ')

#compare and reply
if favorite_animal.lower() == user_animal.lower():
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite') 

"""print('For my own learning purposes: ')   
print(favorite_animal)
print(favorite_animal.lower())
print(user_animal)
print(user_animal.lower())"""



# Formulas needed to complete the task: