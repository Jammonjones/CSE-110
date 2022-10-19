#libraries to be used:
import time

#list variables
shop_list = []

# Variables to be used: 
shop_list_length = 0
quit = 'no'
item = ''
num_item = 0
while quit.lower() != 'quit':
    item = input('Type the item you would like to add to your shopping list: ')
    shop_list.append(item)
    quit = input('Type any letter to add another item or type "quit" to quit: ')
print('The shopping list is: ')
for item in shop_list:
    print(item)

print('The shopping list with indexes is: ')
shop_list_length = len(shop_list)
for i in range(shop_list_length):
    print(f'{i}. {shop_list[i]}')

num_item = int(input('What item do you want to change? '))
new_item = input('What is the new item? ')
shop_list[num_item] = new_item
print('The shopping list with indexes is: ')
for i in range(shop_list_length):
    print(f'{i}. {shop_list[i]}')

time.sleep(15)


