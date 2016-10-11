# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    #NEED TO REWRITE - VERY HACKY CODE
    numofletterstrue = 0
    for i in lettersGuessed:
        if i in secretWord:
            numofletterstrue += 1
    if numofletterstrue == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    result = ""
    for i in secretWord:
        if i in lettersGuessed:
            result += str(i) + ' '
        else:
            result += '_ '
    return result
        
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # Alfabet als string, had ook import string kunnen gebruiken
    alleletters = string.ascii_lowercase
    # Loop door elke gerade letters
    for i in lettersGuessed:
        #Als de geraden letter voorkomt in alleletters, verwijder deze.
        if i in alleletters:
            alleletters = alleletters.replace(i, "")
    #Return om te kijken of alle geraden letters zijn verwijderd uit het alfabet
    return alleletters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #Hangman variabelen
    lettersGuessed = ''
    mistakesMade = 0
    amountGuessesLeft = 8
    lettersGuessed = []
    Dots = '-------------'

    #Start spel prints
    print(str(secretWord) + ": test purposes")
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) +  ' letters long.')
    print(Dots)
    
    #Begin loop, einde loop als iswordGuessed true is of teveel fouten zijn gemaakt
    while ((mistakesMade < 8) and (not isWordGuessed(secretWord, lettersGuessed))):
        
        #Loop prints
        print('You have ' + str(amountGuessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
                
        #Input vragen voor een letter
        pickedLetter = input('Please guess a letter: ')
        pickedLetter = pickedLetter.lower()
        if pickedLetter.isalpha():
            #Check of het al geraden is
            if pickedLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))  
            #Check of de letter in het te-raden-woord zit
            elif pickedLetter in secretWord and not lettersGuessed:
                lettersGuessed.append(pickedLetter)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            #Anders is de letter fout. +1 fout
            else:
                mistakesMade += 1
                amountGuessesLeft -= 1
                lettersGuessed.append(pickedLetter)
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print(Dots)            
        #Wanneer geen geldige letter wordt ingevoerd bij input
        else:
            print('No letter defined. Guess again')

    #Einde van het spel
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)

#Om het script uit te voeren
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
