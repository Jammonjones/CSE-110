with open("C:/Users/jaj2k/Downloads/hr_system.txt") as data:
    for line in data:
        line_name = line.split()
        print(f'{line_name[0]}, {line_name[2]}')
        
        
            