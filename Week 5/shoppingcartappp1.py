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
list_len = 0
item_del = 400
cart_total = 0
add = 'y'
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
        add = 'y'
        while add.lower() == 'y':
            item = input('Enter the name of the item that you would like to add to your cart: ')
            items.append(item)
            price = float(input(f'What is the price of the item: {item} ? '))
            prices.append(price)
            print(f'"{item}" has been added to your cart.')
            add = input('Type "y" to add another item to your cart and a "n" to go back to the menu: ')
    elif menu_sel == 2:
        list_len = len(items)
        print('The items currently in your cart are: ')
        adjustedi = 0
        for i in range(list_len):
            adjustedi = adjustedi + 1
            print(f'{adjustedi}. {items[i]}: ${prices[i]:.2f}')

    elif menu_sel == 3:
        item_del = int(input('Which item would you like to remove? '))
        if item_del > list_len:
            print('Sorry that is not a valid number.')
        else:
            items.pop(item_del-1)
            prices.pop(item_del-1)
            print('Item removed')
    elif menu_sel == 4:
        cart_total = 0
        list_len = len(items)
        for i in range(list_len):
            cart_total = cart_total + prices[i]
        print(f'Your cart total is: ${cart_total:.2f}')
    elif menu_sel == 5:
        quit()
    else:
        print('Please enter a number from 1 to 5')
