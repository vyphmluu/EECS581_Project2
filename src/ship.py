"""
Name: ship.py
Description: This contains our ship class, which holds the size and number of hits on the ship
             We only have two simple functions, to check if a ship is sunk and to add a hit to the ship
Authors: Carson Treece, ...
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/9/2024
"""

class Ship:
    def __init__(self, size):
        self.size = size # record size of the ship
        self.hits = 0 # record number of hits on the ship

    def is_sunk(self):
        return self.hits == self.size # check if sunk by seeing if hits equals size

    def hit(self):
        self.hits += 1 # add a hit to the ship