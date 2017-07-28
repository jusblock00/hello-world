#!/usr/bin/env python
import random

#UNUSED CODE FROM PRESENTATION SLIDE
#def display_message(status):
    #if status == 'right':
       #print 'you guessed it'
    #else:
        #print 'guess too', status

#generate a random number from 1 to 10
n = random.randint(1,10)

#keep running until number is guessed
while True:
    print ('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print 'Your guess is too low'
    elif guess > n:
        print 'Your guess is too high'
    else:
        print 'You guessed the number'
        break
    
