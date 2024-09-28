"""
Name: battleship.py
Description: This is the main initialization file for the game, we are creating the players, ships, and the board.
             This is also where the main loop takes place
Authors: Carson Treece, Zachary Craig, Joshua Park
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/12/2024 (Modified for AI Integration)
"""

from player import Player, AIPlayer  # Added AIPlayer
from board import Board
from ship import Ship
import os
import re


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Determines the ship sizes based on the number of ships and returns the values in a list {1,2,3,4,5}
def get_ship_size(num_ships):
    return [i for i in range(1, num_ships + 1)]


# Main loop for the game
def main():
    cls()

    print("Welcome to Battleship!")

    # Initialize the ship counts
    player1ShipCount = 0
    player2ShipCount = 0

    # Ask Player 1 for number of ships
    while True:
        userInput = input("Player 1, Please Enter the number of ships (between 1-5): ")  # Ask for input

        if re.match("^[12345]$", userInput):  # Check if the input is a number between 1 and 5
            player1ShipCount = int(userInput)  # Convert the input to an integer
            break  # Exit the loop
        else:
            cls()
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

    # Ask Player 2 or AI opponent for number of ships
    opponent_type = input("Would you like to play against a 'human' or 'AI' opponent?: ").lower()

    if opponent_type == 'human':
        while True:
            userInput = input("Player 2, Please Enter the number of ships (between 1-5): ")  # Ask for input

            if re.match("^[12345]$", userInput):  # Check if the input is a number between 1 and 5
                player2ShipCount = int(userInput)  # Convert the input to an integer
                break  # Exit the loop
            else:
                cls()
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
    else:
        # AI will automatically place ships based on the number entered by Player 1
        player2ShipCount = player1ShipCount
        ai_difficulty = input("Choose AI difficulty: 'easy', 'medium', 'hard': ").lower()

    # Create players or AI
    p1 = Player("Player 1", player1ShipCount)

    if opponent_type == 'human':
        p2 = Player("Player 2", player2ShipCount)
    else:
        p2 = AIPlayer("AI", player2ShipCount, ai_difficulty)

    # Player 1 places their ships
    print("Player 1, please place your ships.")
    p1.place_ships()

    # Player 2 (or AI) places ships
    if opponent_type == 'human':
        print("Player 2, please place your ships.")
        p2.place_ships()
    else:
        print(f"AI ({ai_difficulty} difficulty) is placing its ships...")
        p2.place_ships()

    cls()

    # Main game loop
    while True:
        cls()
        print("Player 1's turn.\nPlease hit enter to take your turn.", end="")
        input()  # Pause the game for player 1
        p1.attack_opponent(p2)  # Player 1 attacks Player 2

        if p2.is_defeated():  # Check if Player 2 or AI is defeated
            cls()
            print("Player 1 wins!")
            break

        cls()
        print(f"{p2.name}'s turn.\nPlease hit enter to take your turn.", end="")
        input()  # Pause the game for player 2 or AI

        if opponent_type == 'human':
            p2.attack_opponent(p1)  # Player 2 attacks Player 1
        else:
            p2.take_turn(p1)  # AI attacks Player 1

        if p1.is_defeated():  # Check if Player 1 is defeated
            cls()
            print(f"{p2.name} wins!")
            break


if __name__ == "__main__":
    main()
