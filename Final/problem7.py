# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:36:17 2016

@author: DutchCodes
"""

#x = 10 # example x

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    #Nieuwe functie die      
    def result(x):
        total = 0
        exponent = len(L)-1
        for number in L:
#            print('This calculation was ' + str(number) + ' * ' + str(x) + '^' + str(exponent))
            total += (number * (x**(exponent)))
            exponent -= 1
#        print(total)
        return total
    #Zorgt ervoor dat het tweede argument bij general_poly in result wordt geparsed.
    #Je hebt nu een extra object in een functie        
    return result

general_poly([1, 2, 3, 4])(10) # should return 1234