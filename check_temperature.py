# -*- coding: utf-8 -*-
"""check_temperature

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nRXwsCZp5-vaJEjplrhK8bHD3j6PK0Y2
"""

# Check Temperature
#set maximum temperature
max_temp = 75
#get temperature from user using input
current_temp = float(input("Enter the current temperature: "))
#as long as temperature is higher than the maximum allowable temperature
while current_temp > max_temp:
  print("The temperature is too high")
  current_temp = float(input("Adjust the thermostat. Enter the current temperature: "))

#once the temperature is ok
print("The temperature is acceptable.")