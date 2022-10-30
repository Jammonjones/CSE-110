import time
lowest_life = 900
highest_life = -10
high_life_country = ''
low_life_country = ''
high_life_year = ''
low_life_year = ''

with open('life-expectancy.csv') as data:
    data_lines = data.readlines()
    line_length = len(data_lines)
    for i in range(line_length):
        words = data_lines[i].split(',')
        expextancy = words[3]
        try:
            expextonum = float(expextancy)
        except:
            print()
            print('This line of code was skipped since it was just the title line')
            print()
        else:
            if expextonum < lowest_life:
                lowest_life = expextonum
                low_life_country = words[0]
                low_life_year = words[2]
            if expextonum > highest_life:
                highest_life = expextonum
                high_life_country = words[0]
                high_life_year = words[2]
print(f'The overall lowest life expectancy is: {lowest_life} from {low_life_country} in {low_life_year} ')
print(f'The overall highest life expectancy is: {highest_life} from {high_life_country} in {high_life_year}')
print('')

choseny = int(input('What year would you like to know about? '))
avg_life_for_year = 0.00
max_life = 0.000
max_life_c = ''
low_life = 1000.000
low_life_c = ''
sum_lifeex_for_choseny = 0.00
count = 0

with open('life-expectancy.csv') as data:
    data_lines = data.readlines()
    line_length = len(data_lines)
    for i in range(line_length):
        words = data_lines[i].split(',')
        try:
            year = float(words[2])
        except:
            u=9
        else:
            if year == choseny:
                count = count + 1
                sum_lifeex_for_choseny = sum_lifeex_for_choseny + float(words[3])
                if float(words[3]) > max_life:
                    max_life = float(words[3])
                    max_life_c = words[0]
                elif float(words[3]) < low_life:
                    low_life = float(words[3])
                    low_life_c = words[0]
avg_life_for_year = sum_lifeex_for_choseny / count

print(f'For the year: {choseny}: ')
print(f"The average life expectancy across all countries was {avg_life_for_year:.2f}")
print(f'The max life expectancy was in {max_life_c} with {max_life}')
print(f'The min life expectancy was in {low_life_c} with {low_life}')
        
time.sleep(60)
    