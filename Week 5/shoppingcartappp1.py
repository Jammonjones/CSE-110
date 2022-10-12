'''
Purpose: Make a shopping cart utilizing lists
-Ammon Jones

'''
#Libraries that will be used:
import time

#Declaring List Variables Needed
items = []
prices = []

#Declaring Variables needed in the program:
item = ''
price = ''
menu_sel = 0

#Menu for the shopping cart:
while menu_sel != 5:
    print('Type 1 to add a new item: ')
    print('Type 2 to display the contents of the shopping cart: ')
    print('Type 3 to remove an item: ')
    print('Type 4 for the total price for the items in your cart: ')
    print('Type 5 to quit: ')
    #An error happens here if you don't type a number... fix it
    menu_sel = int(input('Enter your choice here: '))
    if menu_sel == 1:
        item = input('Enter the name of the item that you would like to add to your cart: ')
        items.append(item)
        print(f'"{item}" has been added to your cart.')
    elif menu_sel == 2:
        print('The items currently in your cart are: ')
        adjustedi = 0
        for item in items:
            adjustedi = adjustedi + 1
            print(f'{adjustedi}. {item}')
'''
    elif menu_sel == 3:
    elif menu_sel == 4:
    elif menu_sel == 5:
    else:
        print('Please enter a number from 1 to 5')
'''