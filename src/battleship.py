"""
Name: battleship.py
Description: This is the main initialization file for the game, we are creating the players, ships, and the board.
             This is also where the main loop takes place
Authors: Carson Treece, ...
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/9/2024
"""

from player import Player
from board import Board
from ship import Ship

# Determines the ship sizes based on the number of ships and returns the values in a list {1,2,3,4,5}
def get_ship_size(num_ships):
    return [i for i in range(1, num_ships + 1)]

# Main loop for the game
def main():
    print("Welcome to Battleship!")

    # Create our players
    p1 = Player("Player 1")
    p2 = Player("Player 2")

    # Determine the number of ships
    num_ships = int(input("Please Enter the number of ships (between 1-5):")) # User input for number of ships
    while num_ships < 1 or num_ships > 5: # Check if the number of ships is valid
        print("Invalid number of ships. Please enter a number between 1 and 5.") 
        num_ships = int(input("Please Enter the number of ships (between 1-5):")) # Ask for input again

    # Get the ship sizes
    ship_sizes = get_ship_size(num_ships)

    # Player 1 places their ships
    print("Player 1, please place your ships.")
    p1.place_ships(ship_sizes) # needs to be implemented

    # Player 2 places their ships
    print("Player 2, please place your ships.")
    p2.place_ships(ship_sizes) # needs to be implemented

    # now we play the game
    while True:
        print("Player 1's turn.")

        # Player 1 attacks Player 2
        p1.attack_opponent(p2) # needs to be implemented

        # Check if Player 2 is defeated
        if p2.is_defeated(): # needs to be implemented
            print("Player 1 wins!")
            break
            
        print("Player 2's turn.")

        # Player 2 attacks Player 1
        p2.attack_opponent(p1) # needs to be implemented

        # Check if Player 1 is defeated
        if p1.is_defeated(): # needs to be implemented
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    main()