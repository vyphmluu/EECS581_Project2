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
    def place_ships(self): # need to actually implement this
        for ship in range(self.shipCount): # Loop through all ship sizes
            
            shipLocation = list() # Initialize the ship location
            shipOrientation = "" # Initialize the ship orientation
            while(self.board.addShip(ship+1, shipOrientation, shipLocation) == False):
                # clear the screen
                self.cls()
                
                # clear location
                shipLocation.clear()
                
                inputValid = False # Initialize the input valid flag
                # print the board
                self.board.printBoard()
                
                if(self.board.getErr() != ""):
                    print(f"\nError: {self.board.getErr()}\n")
                    self.board.clearErr()
                
                while(inputValid == False):
                    # starting at getting ship's location
                    print(f"Placing ship of size {ship+1} at location (ex: \"F4\"):", end=" ") # Print the size of the ship the player is placing
                    shipLocationString = input() # Get the location of the ship
                    
                    # check if the location is valid
                    if(len(shipLocationString) < 2 or len(shipLocationString) > 3):
                        print("Invalid input. Please enter a letter and a number (ex: \"F4\")")
                        continue
                    
                    # append the location to the list
                    shipLocation.append(shipLocationString[0]) # add the letter to the location
                    shipLocation.append(int(shipLocationString[1:])) # add the number to the location
                    
                    # moving on to orientation
                    print("Placing ship horizontally or vertically (h/v):", end=" ") # Ask the player if the ship is horizontal or vertical
                    shipOrientation = input() # Get the orientation of the ship
                    
                    # check if the orientation is valid
                    if(shipOrientation != "h" and shipOrientation != "v"):
                        print("Invalid input. Please enter h or v.")
                        continue
                    
                    # if we make it here, the input is valid
                    inputValid = True
            

    def attack_opponent(self, opponent):
        attackLocation = list() # Initialize the attack location
        while(opponent.board.attack(attackLocation) == False):
            # clear the screen
            self.cls()
            
            # need to print the attack board
            print("Attack board:")
            opponent.board.printAttackBoard()
            # print the player's board
            print("\n\nYour board:")
            self.board.printBoard()
            
            # clear location
            attackLocation.clear()
            
            # check if there was an error
            if(opponent.board.getErr() != ""):
                print(f"\nError: {opponent.board.getErr()}\n")
                opponent.board.clearErr()
            
            inputValid = False # Initialize the input valid flag
            while(inputValid == False):
                # get the attack location
                print("Enter the location to attack (ex: \"F4\"):", end=" ") # Ask the player for the location to attack
                attackLocationString = input()
            
                if(len(attackLocationString) < 2 or len(attackLocationString) > 3):
                    print("Invalid input. Please enter a letter and a number (ex: \"F4\")")
                    continue
                
                attackLocation.append(attackLocationString[0]) # add the letter to the location
                attackLocation.append(int(attackLocationString[1:])) # add the number to the location
                
                # if we make it here, the input is valid
                inputValid = True
            
            self.cls()
        
        # show updated attack board
        print("")
        opponent.board.printAttackBoard()
        print("Press enter to continue", end="")
        input()
            
                
                
                

    def is_defeated(self): # need to implement this
        return self.board.checkGameOver() # check if the player is defeated by checking if all ships are sunk