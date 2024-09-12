"""
Name: player.py
Description: This file contains our player class, which holds the players name, board, and ships
             This also contains our functions to place ships, attack opponents, and check if the player is defeated
Authors: Carson Treece, Zachary Craig, Joshua Park
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/10/2024
"""

from board import Board
from ship import Ship
import os

class Player:
    def __init__(self, name, shipCount):
        self.name = name
        self.board = Board(shipCount)
        self.shipCount = shipCount

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print(f"Battleship - {self.name}\n")


    # Place the ships on the board
    def place_ships(self): 
        for ship in range(self.shipCount): # Loop through all ship sizes
            # clear the screen
            self.cls()

            # print the board
            self.board.printBoard()

            shipLocation = list()  # Initialize the ship location
            shipOrientation = ""  # Initialize the ship orientation
            
            # We need to get the input beefore calling addShip to avoid the error message
            inputValid = False  # Initialize the input variable
            while not inputValid:

                # clear location
                shipLocation.clear()

                if self.board.getErr() != "":  # Only display the error if it exists
                    print(f"{self.board.getErr()}")
                    self.board.clearErr()

                # Get the location of the ship
                print(f"Placing ship of size {ship+1} at location (ex: \"F4\"):", end=" ")  
                shipLocationString = input()

                # Append the location to the list
                shipLocation.append(shipLocationString[0])  # add the letter to the location
                try:
                    shipLocation.append(int(shipLocationString[1:]))  # add the number to the location
                except:
                    print("Invalid number for the row. Please try again.")
                    continue  # Restart the loop on invalid number input

                # Get the ship's orientation
                print("Placing ship horizontally or vertically (h/v):", end=" ")
                shipOrientation = input().lower()

                # Attempt to place the ship after gathering input
                inputValid = self.board.addShip(ship + 1, shipOrientation, shipLocation)

            

    def attack_opponent(self, opponent):
        attackLocation = list() # Initialize the attack location
        inputValid = False # Initialize the input variable

        while not inputValid or opponent.board.attack(attackLocation) == False:
            
            self.cls() # clear the screen

            # print the attack board and player's board
            print("Attack board:")
            opponent.board.printAttackBoard()
            print("\n\nYour board:")
            self.board.printBoard()

            attackLocation.clear() # clear location

            # check if there was an error
            if opponent.board.getErr() != "":
                print(f"{opponent.board.getErr()}")
                opponent.board.clearErr()

            # get the attack location
            print("Enter the location to attack (ex: \"F4\"): ", end=" ")
            attackLocationString = input().upper()

            # Validate the attack location input
            if len(attackLocationString) < 2 or len(attackLocationString) > 3:
                print("Invalid input. Please enter a letter and a number (ex: \"F4\")")
                continue

            # Append the column (letter) to attackLocation
            attackLocation.append(attackLocationString[0])
            try:
                # Append the row (number) to attackLocation and check if it's a valid number
                attackLocation.append(int(attackLocationString[1:]))
                inputValid = True
            except ValueError:
                print("Invalid number for the row. Please try again.")
                continue

            self.cls() # clear the screen
            
            # If attack is successful, break out of loop
            if opponent.board.attack(attackLocation):
                inputValid = True # Attack is valid
                break
            else:
                inputValid = False # Attack failed, re-enter location

        # show updated attack board
        print("")
        opponent.board.printAttackBoard()
        print("Press enter to continue", end="")
        input()

            
    def is_defeated(self): # need to implement this
        return self.board.checkGameOver() # check if the player is defeated by checking if all ships are sunk