import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Alfabet als string, had ook import string kunnen gebruiken
    alleletters = string.ascii_lowercase
    print(string.ascii_lowercase)
    print(alleletters)
    # Loop door elke gerade letters
    for i in lettersGuessed:
        #Als de geraden letter voorkomt in alleletters, verwijder deze.
        if i in alleletters:
            alleletters = alleletters.replace(i, "")
    #Return om te kijken of alle geraden letters zijn verwijderd uit het alfabet
    print(alleletters)
    return alleletters
    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))