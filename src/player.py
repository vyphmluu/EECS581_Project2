"""
Name: player.py
Description: This file contains our player class, which holds the players name, board, and ships
             This also contains our functions to place ships, attack opponents, and check if the player is defeated
Authors: Carson Treece, ...
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/10/2024
"""

from board import Board
from ship import Ship

class Player:
    def __init__(self, name, num_ships):
        self.name = name
        self.board = Board(num_ships)
        self.ships = []

    # Place the ships on the board
    def place_ships(self, ship_sizes):
        for size in ship_sizes: # Loop through all ship sizes
            # shows the player their board before each ship placement
            self.print_board()

            valid_space = False

            while not valid_space:
                # getting orientation
                orientation = input(f"Would you like to place your {size}-long ship horizontally (h) or vertically (v)?:  ")
                while orientation != 'h' and orientation != 'v':
                    orientation = input("Please input \'h\' or \'v\' for horizontally (h) or vertically (v):  ")
                if (orientation == 'h'):
                    msg = f"Please give the left end of your {size}-long ship in \"column row\" notation: "
                else:
                    msg = f"Please give the top end of your {size}-long ship in \"column row\" notation: "

                # getting location on the board
                location = input(msg).split()
                valid_space = True
                error_code = 0

                # checking if column is a valid input
                if (len(location[0]) > 1) or (not location[0].lower() in "abcdefghij"):
                    error_code += 1
                    valid_space = False
                
                # checking if row is a valid input
                try:
                    location[1] = int(location[1])
                    if location[1] < 1 or location[1] > 10:
                        error_code += 2
                        valid_space = False
                except:
                    error_code += 2
                    valid_space = False

                match error_code:
                    case 1:
                        print("Your column value is invalid")
                        continue
                    case 2:
                        print("Your row value is invalid")
                        continue
                    case 3:
                        print("Your row and column values are invalid")
                        continue
                    case default:
                        pass

                valid_space = self.board.addShip(size, orientation, location)

    def attack_opponent(self, opponent): # need to implement this
        # need to get the position of the attack
        # need to check if the attack is a hit or miss
        # need to ensure that you get to attack again if you hit
        pass

    def is_defeated(self): # need to implement this
        # probably just need a function to check if all ship tiles on board are hit
        pass

    def print_board(self):
        self.board.printBoard()