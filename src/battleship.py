"""
Name: battleship.py
Description: This is the main initialization file for the game, we are creating the players, ships, and the board.
             This is also where the main loop takes place
Authors: Carson Treece, Zachary Craig, Joshua Park
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/10/2024
"""

from player import Player
from board import Board
from ship import Ship
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Determines the ship sizes based on the number of ships and returns the values in a list {1,2,3,4,5}
def get_ship_size(num_ships):
    return [i for i in range(1, num_ships + 1)]

# Main loop for the game
def main():
    cls()
    
    print("Welcome to Battleship!")

    # This code is if both players have the same number of ships
    # # Determine the number of ships
    # num_ships = int(input("Please Enter the number of ships (between 1-5):")) # User input for number of ships
    # while num_ships < 1 or num_ships > 5: # Check if the number of ships is valid
    #     print("Invalid number of ships. Please enter a number between 1 and 5.") 
    #     num_ships = int(input("Please Enter the number of ships (between 1-5):")) # Ask for input again
    #
    # # Get the ship sizes
    # ship_sizes = get_ship_size(num_ships)
    
    # This code is if both players have different number of ships
    # Determine the number of ships for player 1
    player1ShipCount = int(input("Player 1, Please Enter the number of ships (between 1-5):")) # User input for number of ships
    while(player1ShipCount < 1 or player1ShipCount > 5): # Check if the number of ships is valid
        print("Invalid number of ships. Please enter a number between 1 and 5.")
        player1ShipCount = int(input("Player 1, Please Enter the number of ships (between 1-5):")) # Ask for input again
    
    # Determine the number of ships for player 2
    player2ShipCount = int(input("Player 2, Please Enter the number of ships (between 1-5):")) # User input for number of ships
    while(player2ShipCount < 1 or player2ShipCount > 5): # Check if the number of ships is valid
        print("Invalid number of ships. Please enter a number between 1 and 5.")
        player2ShipCount = int(input("Player 2, Please Enter the number of ships (between 1-5):")) # Ask for input again


    # Create our players
    p1 = Player("Player 1", player1ShipCount)
    p2 = Player("Player 2", player2ShipCount)
    

    # Player 1 places their ships
    print("Player 1, please place your ships.")
    p1.place_ships()
    

    # Player 2 places their ships
    print("Player 2, please place your ships.")
    p2.place_ships()
    
    cls()

    # now we play the game
    while True:
        cls()
        print("Player 1's turn.\nPlease hit enter to take your turn.", end="")
        input() # Pause the game for player 1
        
        p1.attack_opponent(p2)# Player 1 attacks Player 2
        
        if p2.is_defeated(): # Check if Player 2 is defeated
            cls()
            print("Player 1 wins!")
            break
        
        cls()
        print("Player 2's turn.\nPlease hit enter to take your turn.", end="")
        input() # Pause the game for player 2
        
        p2.attack_opponent(p1) # Player 2 attacks Player 1
        
        if p1.is_defeated(): # Check if Player 1 is defeated
            cls()
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    main()