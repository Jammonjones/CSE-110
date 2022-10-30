#Libraries
import time
#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#Where,T= Air Temperature (ºF) V= Wind Speed (mph)
temp = float(input('What is the temperature?'))
scale = input('Fahrenheit or Celsius (f/c)? ')
if scale.lower() == 'c':
    temp = (temp * (9/5) + 32)

#Cacl wind chil for multiple wind speeds and displays them. 
def calc_wind_chill(temp):
    windspeed = 0
    for i in range(12):
        windspeed = windspeed + 5
        windchill = 35.74 + (0.6215 * temp) - (35.75 * windspeed ** 0.16) + (0.4275 * temp * windspeed ** 0.16)
        print(f'At tempekrature {temp:.2f}F, a winds speed of {windspeed} mph, the windchill is: {windchill:.2f}F ')

calc_wind_chill(temp)
time.sleep(60)
