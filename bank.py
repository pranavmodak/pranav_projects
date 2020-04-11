# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:59:37 2020

@author:pranav modak
"""

print("Welcome to HDFC bank")
acc_number=input("Enter acount no:")
password=input("Enter password:")
current_balance=int(input("Enter current balance:"))
print("Menu")
print("1. Balance Inquiry")
print("2. Cash deposit")
print("3. Cash withdraw")
print("4. Loan")
print("5. Quit")


while True:
    menu_selection = int(input("Select from menu: "))
    
    if menu_selection == 1:
        print("Your current balance is: " + str(current_balance))
    elif menu_selection == 2:
        deposit_amount = int(input("Enter amount to deposit: "))
        current_balance = current_balance + deposit_amount
    elif menu_selection == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        if withdraw_amount > current_balance:
            print("You dont have that much amount in your current balance")
        else: 
            current_balance = current_balance - withdraw_amount

    elif menu_selection ==4:
        loan_amount = int(input("Enter loan amount: "))
        if loan_amount > current_balance/2:
            print("You are not eligible for loan")
        else:
            current_balance=current_balance+loan_amount
            print("Your current balance is: " + str(current_balance))
            
    elif menu_selection ==5:
          break
      
print("Thank for coming to HDFC bank")
print("Welcome to HDFC bank")
acc_number=input("Enter acount no:")
password=input("Enter password:")
current_balance=int(input("Enter current balance:"))
print("Menu")
print("1. Balance Inquiry")
print("2. Cash deposit")
print("3. Cash withdraw")
print("4. Loan")
print("5. Quit")


while True:
    menu_selection = int(input("Select from menu: "))
    
    if menu_selection == 1:
        print("Your current balance is: " + str(current_balance))
    elif menu_selection == 2:
        deposit_amount = int(input("Enter amount to deposit: "))
        current_balance = current_balance + deposit_amount
    elif menu_selection == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        if withdraw_amount > current_balance:
            print("You dont have that much amount in your current balance")
        else: 
            current_balance = current_balance - withdraw_amount

    elif menu_selection ==4:
        loan_amount = int(input("Enter loan amount: "))
        if loan_amount > current_balance/2:
            print("You are not eligible for loan")
        else:
            current_balance=current_balance+loan_amount
            print("Your current balance is: " + str(current_balance))
            
    elif menu_selection ==5:
          break
      
print("Thank for coming to HDFC bank")

