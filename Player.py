#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from __future__ import division
import collections
import math
from Enum import *

class Player:

    def __init__(self, attack=1, strength=1, defence=1, 
            ranged=1, magic=1, prayer=1, hitpoints=1, ident=None):
        """Parameters are: attack, strength, defence, ranged, 
        magic, prayer, hitpoints"""
        self.attack = attack
        self.strength = strength
        self.defence = defence
        self.ranged = ranged
        self.magic = magic
        self.prayer = prayer
        self.hitpoints = hitpoints

        self.attack_bonus = collections.defaultdict(int)
        self.defence_bonus = collections.defaultdict(int)
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
    
    def set_attack_bonus(self, stab=0, slash=0, crush=0, ranged=0, magic=0):
        self.attack_bonus[ATTACK_TYPES.STAB] = stab
        self.attack_bonus[ATTACK_TYPES.SLASH] = slash
        self.attack_bonus[ATTACK_TYPES.RANGED] = ranged
        self.attack_bonus[ATTACK_TYPES.MAGIC] = magic
        self.attack_bonus[ATTACK_TYPES.CRUSH] = crush

    def set_defence_bonus(self, stab=0, slash=0, crush=0, ranged=0, magic=0):
        self.defence_bonus[ATTACK_TYPES.STAB] = stab
        self.defence_bonus[ATTACK_TYPES.SLASH] = slash
        self.defence_bonus[ATTACK_TYPES.RANGED] = ranged
        self.defence_bonus[ATTACK_TYPES.MAGIC] = magic
        self.defence_bonus[ATTACK_TYPES.CRUSH] = crush

    def set_strength_bonus(self, bonus):
        self.strength_bonus = bonus

    def get_hit_chance(self, opponent):
        attack_roll = self._get_attack_roll()
        defence_roll = opponent._get_defence_roll(self)

        if attack_roll < defence_roll:
            return (attack_roll - 1) / (2 * defence_roll)
        elif attack_roll > defence_roll:
            return 1 - (defence_roll + 1) / (2 * attack_roll)
        else:
            # Equal rolls
            return (attack_roll - 1) / (2 * defence_roll)


    def _get_attack_roll(self):
        if self.attack_type in [ATTACK_TYPES.RANGED]:
            # Calculate ranged attack roll
            raise Exception('Ranged attacks not implemented yet.')
        elif self.attack_type in [ATTACK_TYPES.MAGIC]:
            # Calculate magic attack roll
            raise Exception('Magic attacks not implemented yet.')
        else:
            # Calculate melee attack roll
            effective_attack = self.attack

            if self.attack_style == ATTACK_STYLES.ACCURATE:
                effective_attack += 3

            if PRAYERS.INCREDIBLE_REFLEXES in self.active_prayers:
               # Multiply in 15% attack bonus
                effective_attack *= 1.15

            # Constant adder
            effective_attack += 8
            
            # Apply stats from selected combat style's gear bonuses
            effective_attack += self.attack_bonus[self.attack_type]
            effective_attack = math.floor(effective_attack)
            
            max_roll = effective_attack * (1 + (self.attack_bonus[self.attack_style]/64))
            max_roll = math.floor(max_roll)
            return max_roll
    
    def _get_defence_roll(self, opponent):
        # Defence roll against opponent based on their attack style.
        if opponent.attack_type in [ATTACK_TYPES.RANGED]:
            # Calculate ranged defence roll
            raise Exception('Ranged defence not implemented yet.')
        elif opponent.attack_type in [ATTACK_TYPES.MAGIC]:
            # Calculate magic defence roll
            raise Exception('Magic defence not implemented yet.')
        else:
            # Calculate melee defence roll
            effective_defence = self.defence

            if self.attack_style == ATTACK_STYLES.DEFENSIVE:
                effective_defence += 3

            if PRAYERS.STEEL_SKIN in self.active_prayers:
                effective_defence *= 1.15
             
            # Constant adder
            effective_defence += 8
            
            # Apply item bonuses that defend from opponent's attack style
            effective_defence += self.defence_bonus[opponent.attack_type]
            
            effective_defence = math.floor(effective_defence)
            max_roll = effective_defence * (1 + (self.defence_bonus[opponent.attack_style]/64))
            max_roll = math.floor(max_roll)
            return max_roll

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
        stab_def = 'Stab: %s\n' % self.defence_bonus[ATTACK_TYPES.STAB]
        slash_def = 'Slash: %s\n' % self.defence_bonus[ATTACK_TYPES.SLASH]
        crush_def = 'Crush: %s\n' % self.defence_bonus[ATTACK_TYPES.CRUSH]
        range_def = 'Ranged: %s\n' % self.defence_bonus[ATTACK_TYPES.RANGED]
        magic_def = 'Magic: %s\n' % self.defence_bonus[ATTACK_TYPES.MAGIC]
        def_bonuses = def_header + stab_def + slash_def + crush_def + range_def + magic_def

        bonuses = att_bonuses + def_bonuses

        prayers = sep + 'Active prayers: ' + ', '.join(map(lambda x: PRAYERS.reverse_mapping[x], self.active_prayers))

        return ident + levels + attack_type + style + bonuses + prayers
