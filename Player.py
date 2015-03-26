#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import collections
from Enum import *

class Player:

    def __init__(self, attack, strength, defence, 
            ranged, magic, prayer, hitpoints, ident=None):
        """Parameters are: attack, strength, defense, ranged, 
        magic, prayer, hitpoints"""
        self.attack = attack
        self.strength = strength
        self.defence = defence
        self.ranged = ranged
        self.magic = magic
        self.prayer = prayer
        self.hitpoints = hitpoints

        self.attack_bonus = collections.defaultdict(int)
        self.defense_bonus = collections.defaultdict(int)
        self.strength_bonus = 0

        self.active_prayers = set()
        self.ident = ident
    
    def set_attack_type(self, type):
        """slash, crush, stab, ranged, magic"""
        self.attack_type = type

    def set_attack_style(self, style):
        """accurate, defensive, controlled, long range"""
        self.attack_style = style

    def set_prayer_on(self, prayer):
        """Item from PRAYERS enum is given."""
        self.active_prayers.add(prayer)

    def set_prayer_off(self, prayer): 
        """Item from PRAYERS enum is given."""
        self.active_prayers.remove(prayer)
    
    def set_attack_bonus(stab=0, slash=0, crush=0, ranged=0, magic=0):
        self.attack_bonus[ATTACK_TYPES.STAB] = stab
        self.attack_bonus[ATTACK_TYPES.SLASH] = slash
        self.attack_bonus[ATTACK_TYPES.RANGED] = ranged
        self.attack_bonus[ATTACK_TYPES.MAGIC] = magic

    def set_defence_bonus(stab=0, slash=0, crush=0, ranged=0, magic=0):
        self.defence_bonus[ATTACK_TYPES.STAB] = stab
        self.defence_bonus[ATTACK_TYPES.SLASH] = slash
        self.defence_bonus[ATTACK_TYPES.RANGED] = ranged
        self.defence_bonus[ATTACK_TYPES.MAGIC] = magic

    def set_strength_bonus(bonus):
        self.strength_bonus = bonus

    def do_attack_roll(self):
        if self.attack_type in [ATTACK_TYPES.RANGED]:
            # Calculate ranged attack roll
            raise Exception('Ranged attacks not implemented yet.')
        elif self.attack_type in [ATTACK_TYPES.MAGIC]:
            # Calculate magic attack roll
            raise Exception('Magic attacks not implemented yet.')
        else:
            pass
            # Calculate melee attack roll
            #pass

    def set_player_id(self, ident):
        self.ident = ident
        
    def __repr__(self):
        
        sep = '\n'
        
        ident = 'Player ID: %s' % self.ident + sep

        att = 'Attack: %s\n' % self.attack
        strength = 'Strength: %s\n' % self.strength
        defence = 'Defence: %s\n' % self.defence
        ranged = 'Ranged: %s\n' % self.ranged
        magic = 'Magic: %s\n' % self.magic
        pray = 'Prayer: %s\n' % self.prayer
        hp = 'Hitpoints: %s\n' % self.hitpoints
        levels = sep + att+strength+defence+ranged+magic+pray+hp + sep

        attack_type = 'Attack type: %s\n' % ATTACK_TYPES.reverse_mapping[self.attack_type]
        style = 'Attack style: %s\n\n' % ATTACK_STYLES.reverse_mapping[self.attack_style]

        att_header = '-Attack Bonuses-\n'
        stab_att = 'Stab: %s\n' % self.attack_bonus[ATTACK_TYPES.STAB]
        slash_att= 'Slash: %s\n' % self.attack_bonus[ATTACK_TYPES.SLASH]
        crush_att= 'Crush: %s\n' % self.attack_bonus[ATTACK_TYPES.CRUSH]
        range_att = 'Ranged: %s\n' % self.attack_bonus[ATTACK_TYPES.RANGED]
        magic_att = 'Magic: %s\n' % self.attack_bonus[ATTACK_TYPES.MAGIC]
        strength = 'Strength: %s\n' % self.strength_bonus
        att_bonuses = att_header + stab_att + slash_att + crush_att + range_att + magic_att + strength + sep

        def_header = '-Defence Bonuses-\n'
        stab_def = 'Stab: %s\n' % self.attack_bonus[ATTACK_TYPES.STAB]
        slash_def = 'Slash: %s\n' % self.attack_bonus[ATTACK_TYPES.SLASH]
        crush_def = 'Crush: %s\n' % self.attack_bonus[ATTACK_TYPES.CRUSH]
        range_def = 'Ranged: %s\n' % self.attack_bonus[ATTACK_TYPES.RANGED]
        magic_def = 'Magic: %s\n' % self.attack_bonus[ATTACK_TYPES.MAGIC]
        def_bonuses = def_header + stab_def + slash_def + crush_def + range_def + magic_def

        bonuses = att_bonuses + def_bonuses

        prayers = sep + 'Active prayers: ' + ', '.join(map(lambda x: PRAYERS.reverse_mapping[x], self.active_prayers))

        return ident + levels + attack_type + style + bonuses + prayers
