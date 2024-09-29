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
    # Main loop for the Battleship game
    cls()
    print("Welcome to Battleship!")

    # Initialize ship counts
    player1ShipCount = 0

    # Ask Player 1 to choose the number of ships
    while True:
        userInput = input("Player 1, Please Enter the number of ships (between 1-5): ")
        if re.match("^[12345]$", userInput):
            player1ShipCount = int(userInput)
            break
        else:
            cls()
            print("Invalid input. Please enter a number between 1 and 5.")

    # Ask if Player 2 is a human or AI
    while True:
        opponent_type = input("Would you like to play against a 'human' or 'AI' opponent?: ").lower()
        if opponent_type in ['human', 'ai']:  # Only accept 'human' or 'ai'
            break  # Valid input, exit the loop
        else:
            cls()
            print("Invalid choice. Please type 'human' or 'AI'.")

    # Create Player 1
    p1 = Player("Player 1", player1ShipCount)

    if opponent_type == 'human':
        # If opponent is human, prompt for Player 2's number of ships
        while True:
            userInput = input("Player 2, Please Enter the number of ships (between 1-5): ")
            if re.match("^[12345]$", userInput):
                player2ShipCount = int(userInput)
                break
            else:
                cls()
                print("Invalid input. Please enter a number between 1 and 5.")
        p2 = Player("Player 2", player2ShipCount)

    else:
        # If opponent is AI, set the same number of ships for AI
        player2ShipCount = player1ShipCount
        while True:
            ai_difficulty = input("Choose AI difficulty: 'easy', 'medium', 'hard': ").lower()
            if ai_difficulty in ['easy', 'medium', 'hard']:
                break
            else:
                cls()
                print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")

        # Create AI player with the same number of ships
        p2 = AIPlayer("AI", player2ShipCount, ai_difficulty)

    # Player 1 places their ships
    print("Player 1, please place your ships.")
    p1.place_ships()

    # AI places its ships automatically if AI is the opponent
    if opponent_type == 'human':
        print("Player 2, please place your ships.")
        p2.place_ships()  # Human Player 2 places ships
    else:
        print(f"AI ({ai_difficulty} difficulty) is placing its ships automatically...")
        p2.place_ships()  # AI places ships automatically

    cls()

    # Now we start the main game loop
    while True:
        cls()
        print("Player 1's turn.\nPress enter to take your turn.", end="")
        input()  # Pause for Player 1
        p1.attack_opponent(p2)  # Player 1 attacks

        if p2.is_defeated():
            cls()
            print("Player 1 wins!")
            break

        cls()
        print(f"{p2.name}'s turn.\nPress enter to take your turn.", end="")
        input()  # Pause for Player 2 or AI

        if opponent_type == 'human':
            p2.attack_opponent(p1)  # Player 2's turn
        else:
            p2.take_turn(p1)  # AI's turn

        if p1.is_defeated():
            cls()
            print(f"{p2.name} wins!")
            break



if __name__ == "__main__":
    main()
