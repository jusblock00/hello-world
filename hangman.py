#!/usr/bin/env python
import random

def check_guess(guessed_characters, secret_word):
    num_failed = 0
    for c in secret_word:
        if c in guessed_characters:
            print c
        else:
            num_failed = num_failed + 1
            print '-'
    if num_failed > 0:
        return False
    else:
        return True

secret_word = 'neatest'#, 'nations', 'aerials', 'nearest', 'restart', 'narrate', 'useless']

num_guess = 10

#create an empty list to store the guessed characters
guessed_characters = []
while num_guess > 0:
    guess = raw_input("Guess a character: ")
    print "You have", num_guess, "guesses left"
    #append new guessed character to guess list
    guessed_characters.append(guess)
    #check characters guess so far
    win = check_guess(guessed_characters, secret_word)
    if win:
        print "You win!"
        break
    num_guess = num_guess - 1
if num_guess == 0:
    print "You lose"
    

