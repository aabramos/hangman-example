# Hangman game

import random
import string
import re

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
    totalLetters = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            totalLetters += 1
    if totalLetters == len(secretWord):
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
    guess = []
    for letter in secretWord:
        if letter in lettersGuessed:
            guess.append(letter)
        else:
            guess.append("_")
    return " ".join(guess)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    availableLetters = list(string.ascii_lowercase)
    for letter in set(lettersGuessed):
        if letter in alphabet:
            availableLetters.remove(letter)
    return "".join(availableLetters)
            

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
    mistakesMade = 8
    guess = ""
    allInputs = []
    lettersGuessed = []
    availableLetters = ""
    availableLetters = getAvailableLetters(availableLetters)
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print ("-------------")
    
    while mistakesMade > 0:
        print ("You have " + str(mistakesMade) + " guesses left.")
        print ("Available Letters: " + availableLetters)
        guess = input ("Please guess a letter: ").lower()
        if not re.match("^[a-z]*$", guess) or len(guess) > 1 or guess == "":
            print ("Error: Only 1 letter a-z allowed!")
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif guess in secretWord:
                lettersGuessed.append(guess)
                allInputs.append(guess)
                print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print ("-------------")
                    break
                availableLetters = getAvailableLetters(allInputs)
            else:
                allInputs.append(guess)
                print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                availableLetters = getAvailableLetters(allInputs)
                mistakesMade -= 1
 
        print ("-------------")
        
    if mistakesMade > 0:
        print ("Congratulations, you won!")
    else:
        print ("Sorry, you ran out of guesses. The word was " + secretWord + ".") 


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)