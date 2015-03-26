#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Player import Player
from Enum import *

if __name__ == '__main__':

    #them = Player(60, 99, 99, 99, 99, 52, 99)
    #print them

    me = Player(99, 99, 45, 99, 99, 52, 99, ident='Nightly Glow')

    # Set up attack styles
    me.set_attack_style(ATTACK_STYLES.ACCURATE)
    me.set_attack_type(ATTACK_TYPES.SLASH)

    # Set up prayers, potions, etc
    me.set_prayer_on(PRAYERS.INCREDIBLE_REFLEXES)
    me.set_prayer_on(PRAYERS.ULTIMATE_STRENGTH)
    me.set_prayer_on(PRAYERS.STEEL_SKIN)

    me.do_attack_roll()

    print me
