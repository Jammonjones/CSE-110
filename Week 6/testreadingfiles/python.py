'''with open('testreadingfiles/banana.txt') as bogus:
    file_list = bogus.readlines()
    length = len(file_list)
    for i in range(length):
        print(file_list[i], end = '')
'''
ttt = 'Hi my name is'
xxx = ttt.split()
for word in xxx:
    print(word)

with open('testreadingfiles/banana.txt') as words:
    for line in words:
        print(line, end = '')


