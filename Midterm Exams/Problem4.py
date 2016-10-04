def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Algemene variabelen
    num = int(num)
    exponent = 0
    result = 0
    
    #Variabelen voor het checken of de exponent dichtbij is
    difference = 0
    closestnumber = num
    closestexponent = 0
    if base > 1: #Integer moet meer dan 1 zijn
        for i in range(1,num): #Loop door alle opties heen, CRUDE
            #Reken het resultaat en verschil uit met num
            result = base ** exponent 
            difference = (abs(num - result))
            #Als het verschil dichterbij is met closestnumber, update closestexponent met huidige exponent
            if difference < closestnumber:
                closestnumber = difference
                closestexponent = exponent
            #Increment exponent zodat de loop incrimenteert
            exponent += 1
        return closestexponent #return closestexponent wanneer loop is geeindigd