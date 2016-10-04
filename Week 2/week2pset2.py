# -*- coding: utf-8 -*-
"""
Taak: 
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
Conditions:
The monthly payment must be a multiple of $10 and is the same for all months.
"""

debt = False
balance = 3240
annualInterestRate = 0.04
monthlyPaymentRate = 10
monthlyInterestRate = annualInterestRate / 12.0

while debt == False: 
    # Nieuwe variabele om balans mee te updaten
    newBalance = balance    
    # Loop door elke maand
    for month in range (1,13):
        # Nieuwe balans uitrekenen
        newBalance -= monthlyPaymentRate
        newBalance =  newBalance + (monthlyInterestRate * newBalance)        
    # MonthlyPaymentRate verhogen indien balans > 0
    if newBalance > 0:
        monthlyPaymentRate += 10
    # Wanneer de balans is afgelost, print de balance + maandrente en verander debt naar True
    elif newBalance < 0:
        print("Lowest Payment: " + str(monthlyPaymentRate))
        debt = True
    # Error handling
    else:
        print("Error")
        break