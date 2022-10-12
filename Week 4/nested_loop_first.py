quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
quote_length = len(quote)
modulator = 10
while modulator < 1 or modulator > 5:
    modulator = int(input('Please enter a number from 1 to 5: '))

for index in range(quote_length):
    if index % modulator == 0:
        print(quote[index].upper(), end = '')
    else:
        print(quote[index].lower(), end = '')



'''list = ['One','two','three']

for word in list:
    print(end = ' ')
    for letter in word:
        print(letter, end = '')

for index in range(3):
    print('')
    word = 'commitment'
    cap_let = input('Out of the letters in the word: commitment, which one do you want to be capitalized?')
    print('')
    for letter in word:
        if letter == cap_let.lower():
            print('_',end = '')
        else:
            print(letter, end = '')

first_name = 'Brighton'
first_name_length = len(first_name)
for index in range(first_name_length):
    print(index, end = '')
    print(first_name[index])
            '''


        
