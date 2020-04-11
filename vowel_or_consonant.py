# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:38:51 2020

@author: pranav modak
"""
print("Enter any letter I will tell it is a vowel or a consonant")
letter=input("Enter letter: ")
#if letter.equals('a') or letter.equals('e') or letter.equals('i') or letter.equals('o') or letter.equals('u'): 
if letter == "a" or  letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter is a vowel")
else:
    print("The letter is consonant")