"""
File: unit_conversion
Author: Ammon Jones

Purpose: Convert degrees from F to C
"""
temp = float(
input('Please enter the temperature: '))
temp_cels = (temp - 32) * (5/9)
print(f'The temperature in celsius is: {temp_cels:.1f}')