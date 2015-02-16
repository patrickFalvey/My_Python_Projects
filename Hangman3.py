import random
import string
import time
import re,sys
WORDLIST_FILENAME = "words.txt"

##Acces text file 
def load_words():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

##Choose a word from text file at random
def choose_word(wordlist):
    global words
    words = random.choice(wordlist)
    return words
wordlist = load_words()
chosenWord = choose_word(wordlist)
chosenWord = chosenWord.upper()
correctAnswer = chosenWord
print correctAnswer
spaces = len(chosenWord)
tries = (spaces * 2)
alph = ''
letter = ''
status = ''
correct = ''

def welcome():   
    print """**************************************WooHoo!**********************************
Welcome to Patricks' Hangman-umble version 1.0!!!
    A simple game that is a combination of both hangman and a word jumble.
Guess the word before you run out of tries and you will win yourself some
shillings!
    The game has picked a random word with """ + str(spaces) + """ letters in it.
You will have """ + str(tries) + """ tries to guess the word.
*******************************************************************************""" 
welcome()

##Check to see if the user is ready to play.
def readyCheck(status):
    while True:
        status = raw_input("""\n*******************************READY TO PLAY????*****************************
Type YES or NO?:""")
        status = status.lower()
        status = status.replace(' ', '')
        
        if status == 'yes':
            print 'Allrighty then!'
            return True
        elif status == 'no':
            print"""Well too bad, we are going to play anyway......cause I want to."""
            time.sleep(4)
            print"""*****************************************************************************
Just joking.  This 'game' will shutdown in 7 seconds.
On behalf of Hangman-umble Games'tm', thank you for playing.   :)"""
            time.sleep(7)
            sys.exit()
        elif status.isalpha() == False:
            print"""Those ain't all letters in there!
Dude....yes or no.  All caps or all mixed up, doesn't matter just pick one.
So, pretty please, with a cherry on top.  Yes or No please:"""
                
        elif status.isalpha():
            print"Looks like someone needs a little spelling refresher... Lets try that again..."

##Entire game process
def runGame(letter):
    global chosenWord
    global tries
    lettersLeft = chosenWord
    spaces = 0
    counter = 0
    correct = ''
    alph = 'ABCD EFGH IJKL MNOP QRST UVWX YZ'
    while True:
        if len(lettersLeft) == 0:
            return lettersLeft
            
        elif counter == tries:
            print 'You appear to have lost...'
            return chosenWord
            
        else:
            if len(correct) > 0:
                print 'Here are the letters that you have discovered in the jumble: ' + str(correct)
            print "\nLetters that you haven't guessed yet: " + alph
            time.sleep(.5)
            letter = str(raw_input('\nPlease guess a letter that you think may be in the word:'))
            letter = letter.replace(' ','')
            letter = letter.upper()                        
            time.sleep(.5)
            counter += 1

            ##Determine wherther is a valid guess.
            ##Deliver appropriate response and restructure variables accordingly.
            def isValidGuess(alph, letter, lettersLeft, correct):
                if letter.isalpha():
                    if letter in alph and letter in lettersLeft:
                        print 'letter = ' + str(letter)
                        alph = alph.replace(str(letter), '')
                        correct += letter
                        lettersLeft = lettersLeft.replace(letter,'')
                        return alph, lettersLeft, correct, letter, True 
                        
                    elif letter in alph and letter not in lettersLeft:
                        print"Sorry, but that letter isn't in the word."
                        return alph, lettersLeft, correct,letter, True
                    else:
                        print "Sorry, but you've already guessed " + str(letter) + '.'
                        return alph, lettersLeft, correct,letter, True
                else:
                    print 'Hey man!  That aint no Letter!'
                    return alph, lettersLeft, correct, letter, True
                
            
            alph, lettersLeft, correct, letter, aValidGuess = isValidGuess(alph, letter, lettersLeft, correct)
                    
if readyCheck(status):
    wordLeft = runGame(letter)
    
##Check result of game.
def winCheck(wordLeft):
    wordLeft = str(wordLeft)
    if len(wordLeft) == 0:
        print """\n((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
!!!!!!!!!!!!!!!!!You guessed it, the word was """ + str(chosenWord) + """!!!!!!!!!!!!!!!!!
Congratulations my friend! You are champion and have won three Schillings!!!
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("""
    else:
        print """!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!OH NO!!!!  You have ran out of guesses for this game.\n**********************Game Over******************
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
    
winCheck(wordLeft)


