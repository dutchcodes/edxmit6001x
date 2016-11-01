# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 08:33:56 2016

@author: DutchCodes
"""
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
         '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
         
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    #Algemene variabelen, split ook het nummer in tweeën en zoekt daarbij de key van dictionary trans op
    choppedString = str(us_num)
    lastDigitWord = trans.get(choppedString[-1:])
    firstDigitWord = trans.get(choppedString[:1])
    us_num = int(us_num) #Nodig voor EDX grader, anders type error

    #Daadwerkelijke functie          
    if us_num < 11: #Voor alles tm 11
        return trans.get(choppedString)
    #Voor alle getallen, meervoud van 10
    elif us_num % 10 == 0:
        return firstDigitWord + ' shi'
    #Alles tussen 11-20
    elif us_num > 10 and us_num <21:
        return 'shi ' + lastDigitWord
    #Vanaf >21
    else:
        return firstDigitWord + ' shi ' + lastDigitWord
              
#convert_to_mandarin('36') will return san shi liu
#convert_to_mandarin('20') will return er shi
#convert_to_mandarin('16') will return shi liu