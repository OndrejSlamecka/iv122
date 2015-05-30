#!/usr/bin/env python3

from random import randint

"""
 An experimental evaluation of the Monty Hall problem, that is
 a game between a player and Monty

 https://xkcd.com/1282/
"""

N = 1000*1000  # Repeat the experiment N times

def problem_instance(): return [0,1,2]

def unveil_door(treasure, guess):
    """
     Monty unveils the single door which
       a) was not picked by the player,
       b) do not contain the treasure
    """
    s = problem_instance()
    s.remove(guess)
    if treasure in s:
        s.remove(treasure)
        return s[0]
    else:
        return s[randint(0,1)]  # randint range is inclusive

def smart_player(guess, door_shown_by_monty):
    """
     The strategy of the smart player is to always change his choice
     to the door which was a) not shown by Monty, b) not the first choice
    """
    s = problem_instance()
    s.remove(guess)
    s.remove(door_shown_by_monty)
    return s[0]

def random_player(door_shown_by_monty):
    """
     The strategy of the smart player is to always change his choice
     to the door which was a) not shown by Monty, b) not the first choice
    """
    s = problem_instance()
    s.remove(door_shown_by_monty)
    return s[randint(0,1)]

def mh():
    """
    Emulate one round of the Monty Hall game.
    """

    # Create the doors and place the treasure
    s = problem_instance()
    treasure = randint(0,2)

    # The player picks a door
    guess = randint(0,2)

    # Monty unveils one door

    door_to_show_to_player = unveil_door(treasure, guess)

    ## We proceed to emulate three different strategies of the player
    success = [0,0,0]  # Vector of success of each strategy

    # Smart player
    door_to_pick = smart_player(guess, door_to_show_to_player)

    if door_to_pick == treasure:
        success[0] += 1

    # Not so smart player
    door_to_pick = guess

    if door_to_pick == treasure:
        success[1] += 1

    # Mr. Random
    door_to_pick = random_player(door_to_show_to_player)

    if door_to_pick == treasure:
        success[2] += 1

    return success

###

if __name__ == "__main__":
    success = [0,0,0]  # Vector of success of each strategy
    for i in range(N):
        success = list(map(sum, zip(success, mh())))

    print('Smart:', success[0], '/', N, '=', success[0] / N * 100, '%')
    print('Stay:', success[1], '/', N, '=', success[1] / N * 100, '%')
    print('Random:', success[2], '/', N, '=', success[2] / N * 100, '%')

