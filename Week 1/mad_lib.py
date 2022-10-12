"""
Program: Mad Lib Story
Purpose: Make a funny story with input from user.
Creator: Ammon Jones
Date: 09/17/22
 
"""
#Constants:
 
#variables:
adjective=0
animal=0
verb=0
exclamation=0
verb1=0
verb2=0
again=0
yes='y'

#Main Code:

#Input needed from user
print('Hey thanks for coming to play this fun story game! Please enter the words as prompted and we will generate a fun story for you to read using the words of your choice!')
print('Please enter the following:')
adjective = input('An adjective ')
animal = input('An animal ')
verb = input('A verb ')
exclamation = input('An exclamantion ')
verb1 = input('A verb ')
verb2 = input('Another verb ')

#Output story to user
print('Here is your story:')
print(f' The other day, I was really in trouble. It all started when I saw a very\n {adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all\n I could think to do was to {verb1} over and over. Miraculously,\n that caused it to stop, but not before it tried to {verb2}\n right in front of my family.')

#give option to run the code again
print('Did you like this story? Type y for yes and n for no')
again=input()
if again == 'y': 
    print('We are so glad that you liked it!')
else:
    print('Sorry that you did not like it')
import time
time.sleep(15)

    








