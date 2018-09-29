"""
Sample project. Guess game. The goal is to guess number on rolled dice.
"""

from random import randint
from time import sleep


def get_user_guess():
  user_guess = int(raw_input('What is the number?'))
  return user_guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  
  print "Max value is %d" % (max_val)
  #simulate thinking
  sleep(1)
  
  user_guess = get_user_guess()
  
  if user_guess > max_val:
    print "We don't play like this, max is: %d" % max_val
    return
  else:
    print "Rolling!"
    sleep(2)
    print "First roll is: %d" % first_roll
    sleep(2)
    print "Second roll is: %d" % second_roll
    
    total_roll = first_roll + second_roll
    print "Result is: %d" % total_roll
    
    if user_guess > total_roll:
      print "You WON!"
    else:
      print "You LOST!"
    return
    
    
roll_dice(6)
