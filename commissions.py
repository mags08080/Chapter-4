# -*- coding: utf-8 -*-
"""commissions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dOiQPhsG2DZiWMoqJOvC8rHZYxTZM2MM
"""

##calcuate a series of commissions

#create a variable to control while loop
keep_going = 'y'
#while loop
while keep_going == 'y':
#get a salesperson's sales and commission rate using input functions
  sales = float(input("Enter the salesperson's sales amount: "))
  rate = float(input("Enter the commission rate: "))
#calculate the commission
  commission = sales * rate
#display the commission
  print("The salesperson's commission is:", commission)
#ask if the user wants to do another one
  keep_going = input("Do you want to calculate another commission (enter y for yes): ") #if it is anything other than y will terminate