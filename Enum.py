#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

ATTACK_STYLES = enum('ACCURATE', 'AGGRESSIVE', 'DEFENSIVE', 'CONTROLLED', 'LONGRANGE')
ATTACK_TYPES = enum('STAB', 'SLASH', 'CRUSH', 'RANGED', 'MAGIC')
PRAYERS = enum('INCREDIBLE_REFLEXES', 'ULTIMATE_STRENGTH', 'STEEL_SKIN', 'EAGLE_EYE', 'MYSTIC_MIGHT')
LEVELS = enum('ATTACK', 'STRENGTH', 'DEFENCE', 'RANGED', 'MAGIC', 'PRAYER', 'HITPOINTS')
