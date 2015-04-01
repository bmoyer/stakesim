#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Player import Player
from Enum import *
import random

def setup_players():
    # Create my player
    me = Player(attack=99, strength=99, defence=99, ranged=99, magic=99, prayer=99, hitpoints=99, ident='you')
    me.set_attack_style(ATTACK_STYLES.ACCURATE)
    me.set_attack_type(ATTACK_TYPES.CRUSH)
    me.set_attack_bonus(slash=0, stab=0, crush=0)

    # Create basic opponent
    them = Player(attack=99, strength=99, defence=99, ranged=99, magic=99, prayer=99, hitpoints=99, ident='them')
    them.set_attack_style(ATTACK_STYLES.AGGRESSIVE)
    them.set_attack_type(ATTACK_TYPES.SLASH)
    them.set_defence_bonus(crush=0, stab=0, slash=0)
    
    return me, them

def run_simulation(player1, player2):
    tick = 0
    # Roll to see who gets the first hit
    first_hit_roll = random.random()
    if first_hit_roll > 0.5:
        # player1 gets the first hit
        player1.do_attack(player2)
        while((player1.hitpoints > 0) and (player2.hitpoints > 0)):
            player2.do_attack(player1)
            player1.do_attack(player2)
    else:
        # player2 gets the first hit
        player2.do_attack(player1)
        while((player1.hitpoints > 0) and (player2.hitpoints > 0)):
            player1.do_attack(player2)
            player2.do_attack(player1)
    
    if(player1.hitpoints <= 0):
        print player1.ident, ' won!'
        return 1
    else:
        print player2.ident, ' won!'
        return 0

if __name__ == '__main__':

    me, them = setup_players()
    run_simulation(me, them)
