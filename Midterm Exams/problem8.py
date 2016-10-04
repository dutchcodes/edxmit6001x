def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Maak een nieuwe lijst
    L_mutated = []
    # Start loop op L die buiten de function staat
    for i in L:
        # Check of g(f(i)) = true. Ja --> voeg de huidige loop i toe aan mutated list
        if g(f(i)):
            L_mutated.append(i)
    # Mutate normale lijst L zodat het een nieuwe kopie van mutated_L binnen de functie
    L[:] = L_mutated
     # Check of mutated list leeg is. Ja --> return -1       
    if L_mutated == []:
        return -1
    #Return maximale waarde van L_mutated
    else:
        return max(L_mutated)

#Voorgeleverde functies
def f(i):
    return i + 2
def g(i):
    if i > 5:
        return True
    else:
        return False
        
#Om het programma mee te starten
L = [0, -10, 5, 10, -4]    
print(applyF_filterG(L, f, g))

