print "Time to play a guessing game!"

from random import randrange
random = randrange(1, 100)
print "The computer has now guessed a number!"
guess_number = int(0)
guess = ""
while guess != random:
    guess_number += 1
    guess = int(raw_input("Please enter a number between 1 and 100."))
    if guess > random:
        print "Too high, guess again: " + str(guess)
    else:
        print "Too low, guess again: " + str(guess)
print "You got it!  Hooray!!!  It only took you " + str(guess_number) + " guesses."
    
    
