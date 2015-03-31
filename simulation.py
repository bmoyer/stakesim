#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Player import Player
from Enum import *

if __name__ == '__main__':

    # Create my player
    me = Player(attack=99, strength=99, defence=99, ranged=99, magic=99, prayer=99, hitpoints=99)
    me.set_attack_style(ATTACK_STYLES.ACCURATE)
    me.set_attack_type(ATTACK_TYPES.CRUSH)
    me.set_attack_bonus(slash=0, stab=0, crush=0)

    # Create basic opponent
    them = Player(attack=99, strength=99, defence=99, ranged=99, magic=99, prayer=99, hitpoints=99)
    them.set_attack_style(ATTACK_STYLES.AGGRESSIVE)
    them.set_attack_type(ATTACK_TYPES.SLASH)
    them.set_defence_bonus(crush=0, stab=0, slash=0)

    chance = me.get_hit_chance(them)
    print 'Hit chance: ', chance
