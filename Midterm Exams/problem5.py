# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:20:16 2016

@author: Jordy
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    #Algemene Variabelen
    total =  0
    #Start de loop met als eindpunt de lengte van listA. 
    for i in range(len(listA)):
        #Vermenigvuldig beide indexxen van elke lijst met elkaar en voeg die toe aan totaal
        multiplied = listA[i] * listB[i]
        total += multiplied
    #Return het totaal
    return total
        
    
#dotProduct([-69, -54, 42, 64, -33, 87, 28, 45, -20], [55, 100, 95, -87, -31, -53, 21, 23, 23])
#correcte output = -13198