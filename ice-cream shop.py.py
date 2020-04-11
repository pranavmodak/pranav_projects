# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:34:14 2020

@author: pranav modak
"""

print("welcome to shahi ice-cream shop")
print("1:mango ice-cream -$2")
print("2:choclate ice-cream -$1")
print("3:pineapple ice-cream -$3")
print("4:butterscotch ice-cream-$4")

do = 'yes'
price=0

while do == 'yes':
      item=int(input("enter item"))
      if item == 1:
         price = price + 2
      if item == 2:
          price = price + 1
      if item ==3:
          price = price + 3
      if item == 4:
          price = price + 4
      do=input("do you want more ice-cream?select yes or no:")
print ("total price is: " + str (price))