# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:20:48 2016

@author: Jordy
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

fancy_divide([0, 2, 4], 0)