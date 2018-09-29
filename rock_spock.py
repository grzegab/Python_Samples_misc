"""
Sample project. Game Rock Paper Scissors Lizard Spock as seen in The Big Bang Theory.

Rules:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors

"""
from datetime import datetime
from time import sleep
from random import randint

items = {
    1: "Scissors",
    2: "Paper",
    3: "Rock",
    4: "Lizard",
    5: "Spock"
}


def start_instructions():
    now = datetime.now()
    print "Let the game begin! (at %s-%s-%s)" % (now.day, now.month, now.year)
    print
    sleep(1)
    print "Things that could be selected:"
    print
    for item in items:
        print "%d is for %s" % (item, items[item])


def random_select():
    max_value = len(items)
    random = randint(1, max_value)
    return random


def user_input_check(user_input):
    try:
        val = int(user_select)
    except ValueError:
        print("That's not an select! We selected for you:")
        return random_select()

    if val < 1 or val > len(items):
        print("That's not an select! We selected for you:")
        return random_select()

    return val


def win_message(item_int):
    print "You won! %s wins!" % items[item_int]


def result(user_select, computer_select):
    print "You selected: %s" % items[user_select]
    print
    print "Computer selected: "
    sleep(2)
    print str(items[computer_select])
    print
    if user_select == computer_select:
        print "Nobody. It's a tie!"
    elif user_select == 1 and computer_select in [2, 4]:
        win_message(user_select)
    elif user_select == 2 and computer_select in [3, 5]:
        win_message(user_select)
    elif user_select == 3 and computer_select in [1, 4]:
        win_message(user_select)
    elif user_select == 4 and computer_select in [2, 5]:
        win_message(user_select)
    elif user_select == 5 and computer_select in [1, 3]:
        win_message(user_select)
    else:
        print "You lost!"


start_instructions()
computer_select = random_select()
user_select = raw_input('Select one number: ')
# check if user select is ok
user_select = user_input_check(user_select)
result(user_select, computer_select)
