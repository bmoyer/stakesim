#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Player import Player
from Enum import *

if __name__ == '__main__':

    # Create basic opponent
    them = Player(99, 99, 99, 99, 99, 52, 99, ident='Opponent')
    them.set_attack_style(ATTACK_STYLES.ACCURATE)
    them.set_attack_type(ATTACK_TYPES.SLASH)
    them.set_defence_bonus(crush=0)

    # Create my player
    me = Player(99, 99, 99, 99, 99, 52, 99, ident='Nightly Glow')
    me.set_attack_style(ATTACK_STYLES.ACCURATE)
    me.set_attack_type(ATTACK_TYPES.CRUSH)
    me.set_attack_bonus(slash=100, stab=50, crush=0)

    chance = me.get_hit_chance(them)
    print 'Hit chance: ', chance
