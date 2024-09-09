"""
Name: player.py
Description: This file contains our player class, which holds the players name, board, and ships
             This also contains our functions to place ships, attack opponents, and check if the player is defeated
Authors: Carson Treece, ...
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/9/2024
"""

from board import Board
from ship import Ship

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ships = []

    # Place the ships on the board
    def place_ships(self, ship_sizes): # need to actually implement this
        for size in ship_sizes: # Loop through all ship sizes
            # need to pick the orientation and position of the ship
            # dont actually know how to do this yet
            pass 

    def attack_opponent(self, opponent): # need to implement this
        # need to get the position of the attack
        # need to check if the attack is a hit or miss
        # need to ensure that you get to attack again if you hit
        pass

    def is_defeated(self): # need to implement this
        # probably just need a function to check if all ship tiles on board are hit
        pass