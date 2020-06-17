# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:37:01 2020

@author: modak
"""
name={"pranav":"latitude",
      "ninad":"e614",
      "deepali":"DQ",
      "ALOK":"f5"}

user_name=input("enter username")
user_password=input("enter user password")

if user_password==name[user_name]:
    if user_name==name[user_name]:
        print("authenthicated")
    else:
        print("invalid password")