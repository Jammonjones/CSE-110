people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
small_num = 300
young_person = ''
for line in people:
    wordsinlin = line.split()
    try:
        stringtonum = int(wordsinlin[1])
    except:
        y=3
    else:
        if small_num > stringtonum:
            small_num = stringtonum
            young_person = wordsinlin[0]




    
print(f'The youngest person is {young_person} and their age is: {small_num}')
