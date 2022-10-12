"""
File Name: speedofobject.py
Creator: Ammon Jones
Purpose: Determine speed of falling object.
"""
# Libraries needed to complete the task:
import math

# Functions needed to complete the task:

# Constants needed to complete the task:

# Information from user needed to complete the task:
print('To calculate the velocity at time x enter the following information:')
m = float(input('Mass (In kg): '))
g = float(input('Gravity, enter "9.8" for Earth or "24" for Jupiter: '))
t = float(input('Time (In seconds): '))
p = float(input('Density of fluid, enter "1.3" for air or "1000" for water: '))
A = float(input('Cross sectional area of projectile (in square meters): '))
C = float(input('Drag constant, enter "0.5" for sphere or "1.1" for cylinder falling on its side: '))

# Formulas needed to complete the task:
c = .5 * p * A * C
velocity_at_time = (math.sqrt(m * g / c)) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Output to the user.
print(f'The value of c is: {c:.3f}')
print(f'The velocity after {t} seconds is: {velocity_at_time:.3f}')



