# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:06:34 2016

@author: Jordy
"""

balance = 457
annualInterestRate = 0.18
monthlyPaymentRate = 0.05
monthlyInterestRate = annualInterestRate / 12.0

# Loop door elke maand
for month in range (1,13):
    # Minimum aflossing p/maand
    minMonthPay = balance * monthlyPaymentRate
    
    #nieuwe balans uitrekenen
    balance -= minMonthPay
    balance =  balance + (monthlyInterestRate * balance)
    
#print resterende balans    
print("Remaining balance: " + str(round(balance, 2)))