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
    def __init__(self, size, orientation, location):
        self.size = size # record size of the ship
        self.damage = 0 # record number of hits on the ship
        self.orientation = orientation
        self.location = location

    def is_sunk(self):
        return self.damage >= self.size # check if sunk by seeing if hits equals size

    def hit(self):
        self.damage += 1 # add a hit to the ship
        
    def getSize(self):
        return self.size
    
    def getOrientation(self):
        return self.orientation
    
    def getLocation(self):
        return self.location
    
    def getDamage(self):
        return self.damage