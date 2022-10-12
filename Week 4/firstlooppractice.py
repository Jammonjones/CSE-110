#Loop checking for positive number
pos_num = -1
while pos_num <= 0:
    pos_num = float(input('Please type a positive number: '))
    if pos_num <= 0:
        print('Sorry but that is not a positibe number please try again!')
print(f'The number is: {pos_num}')

#Ask for candy until yes...
candy_yes = 'no'
while candy_yes.lower() != 'yes':
    candy_yes = input('Can I have a piece of candy? ')
print('Thank you!!!!')
