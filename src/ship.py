"""
Name: ship.py
Description: This contains our ship class, which holds the size and number of hits on the ship
             We only have two simple functions, to check if a ship is sunk and to add a hit to the ship
Authors: Carson Treece, Zachary Craig
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/9/2024
"""

class Ship:
    def __init__(self, size, orientation, location):
        self.size = size  # record size of the ship
        self.damage = 0  # record number of hits on the ship
        self.orientation = orientation  # record orientation of the ship
        self.location = location  # record location of the ship

    # function to return status of the ship
    def is_sunk(self):
        return self.damage >= self.size  # returns if sunk by seeing if hits equals or exceeds the size

    # function to add damage to its hull
    def hit(self):
        self.damage += 1  # add a hit to the ship

    # function to return the size of the ship
    def getSize(self):
        return self.size  # returns its size
    
    # function to return the orientation of the ship
    def getOrientation(self):
        return self.orientation  # returns its orientation
    
    # function to return the location of the ship
    def getLocation(self):
        return self.location  # returns its location
    
    # function to return the amount of damage the ship has taken
    def getDamage(self):
        return self.damage  # returns its damage
    
    # NEW function to return the list of all coordinates the ship occupies
    def get_coordinates(self):
        # Initialize an empty list to store the ship's coordinates
        coordinates = []
        
        # Get the starting row and column from the location
        row, col = self.location[1] - 1, ord(self.location[0].upper()) - 65  # Convert the letter to an index
        
        if self.orientation == 'v':  # If the ship is placed vertically
            # Add the coordinates vertically based on the ship size
            for i in range(self.size):
                # Append the row with the same column (because it's vertical)
                coordinates.append((self.location[0], self.location[1] + i))  
        else:  # If the ship is placed horizontally
            # Add the coordinates horizontally based on the ship size
            for i in range(self.size):
                # Append the column with the same row (because it's horizontal)
                coordinates.append((chr(ord(self.location[0].upper()) + i), self.location[1]))  
        
        # Return the list of all coordinates occupied by the ship
        return coordinates
