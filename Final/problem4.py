# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:13:04 2016

@author: DutchCodes
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    finalLength = 0
    tempLengthIncr = 0
    tempLengthDecr = 0
    newIncrList = []
    newDecrList = []
    finalList = []
    oldNum = L[0]
    

    X = L[:]
    for i in X:  
        #Als het nieuwe getal groter is dan het oude getal --> monotonically increasing loop
        if i >= oldNum :
            if tempLengthDecr >= 1 and i <= oldNum:
                tempLengthIncr = 0
                tempLengthDecr += 1
                newIncrList = []
                newDecrList.append(i)
                if tempLengthDecr > finalLength:
                    finalLength = tempLengthDecr
                    finalList = newDecrList[:]
#                    print(newDecrList)
                #Verhoog 
            tempLengthDecr = 0
            tempLengthIncr += 1
            newDecrList = []
            newIncrList.append(i)
            if tempLengthIncr > finalLength:
                finalLength = tempLengthIncr
                finalList = newIncrList[:]
#                print(newIncrList)
        #Als het nieuwe getal groter is dan het oude getal --> monotonically decreasing loop
        elif i <= oldNum:
            tempLengthIncr = 0
            tempLengthDecr += 1
            newIncrList = []
            newDecrList.append(i)
            if tempLengthDecr > finalLength:
                finalLength = tempLengthDecr
                finalList = newDecrList[:]
#                print(newDecrList)
        oldNum = i

    totalScore = 0
    for number in finalList:
        totalScore += number
    
    print(totalScore)
    return totalScore
        
longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9]) # Must return 45
longest_run([1, 2, 3, 2, 1]) #Must return 6
longest_run([3, 2, 1, 2, 3]) #Must return 6
longest_run([1, 2, 1, 2, 1, 2, 1, 2, 1]) #Must return 3
longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) #Must return 65
longest_run([1, 2, 3, 2, -1]) #Must return 6
longest_run([100, 200, 300, -100, -200, -1500, -5000]) #Must return -6500
longest_run([100, 200, 300, 400, 0, 10000, 20000]) #Must return 1000
longest_run([3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]) #Must return 11
longest_run([3, 4, 5, 6, 10, 20, 100, 200, 1, 3, 3, 3, -10, 1, 2, 3, 4]) #Must return 348
longest_run([-1, -10, -10, -10, -10, -10, -10, -100]) #Must return 161

