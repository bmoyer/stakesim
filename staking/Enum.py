#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-


def Enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.items())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

ATTACK_STYLES = Enum('ACCURATE', 'AGGRESSIVE', 'DEFENSIVE', 'CONTROLLED', 
    'LONGRANGE')
ATTACK_TYPES = Enum('STAB', 'SLASH', 'CRUSH', 'RANGED', 'MAGIC')
PRAYERS = Enum('INCREDIBLE_REFLEXES', 'ULTIMATE_STRENGTH', 'STEEL_SKIN', 
    'EAGLE_EYE', 'MYSTIC_MIGHT')
LEVELS = Enum('ATTACK', 'STRENGTH', 'DEFENCE', 'RANGED', 'MAGIC', 'PRAYER', 
    'HITPOINTS')
