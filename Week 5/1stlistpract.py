names_friends = []
name = ''

while name != 'end':
    name = input('What is the name of one of your friends? ')
    if name != 'end':
        names_friends.append(name)
print('The names of your friends are: ')
for name in names_friends:
    print(name)
