"""
Name: player.py
Description: This file contains our player class, which holds the players name, board, and ships
             This also contains our functions to place ships, attack opponents, and check if the player is defeated
Authors: Carson Treece, Zachary Craig, Joshua Park
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/12/2024
"""

from board import Board
from ship import Ship
import os
import re
import random  # Added for AI

class Player:
    def __init__(self, name, shipCount):
        self.name = name
        self.board = Board(shipCount)
        self.shipCount = shipCount

    # function to clear the screen
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # makes a system call to clear the screen.
        print(f"Battleship - {self.name}\n")  # print the title of the game every time the screen is cleared

    # check input against regex
    def regexCheck(self, userInput, inputType):
        if (not re.match("^[ABCDEFGHIJabcdefghij]([123456789]|10)$", userInput)) and inputType == "location":  # checks to see if first character is A-J or a-j and second character is 1-10
            return False
        if (not re.match("^[hv]$", userInput)) and inputType == "orientation":  # checks to see if input is h or v
            return False
        return True

    # Place the ships on the board
    def place_ships(self): 
        for ship in range(self.shipCount):  # Loop through all ship sizes
            shipLocation = list()  # Initialize the ship location
            shipOrientation = ""  # Initialize the ship orientation
            
            # We need to get the input before calling addShip to avoid the error message
            inputValid = False  # Initialize the input variable
            while not inputValid:
                # clear the screen
                self.cls()
                # print the board
                self.board.printBoard()
                # clear location
                shipLocation.clear()

                # get the location of the ship
                print(f"Placing ship of size {ship+1} at location (ex: \"F4\"):", end=" ")  # ask for input
                shipLocationString = input()  # get the input

                if self.regexCheck(shipLocationString, "location") is False:  # check the input against the regex
                    print("Invalid ship location. Location should be [A-J][1-10].")  # print error message
                    input("Please press enter to continue...")  # wait for user to press enter
                    continue

                # Append the location to the list
                shipLocation.append(shipLocationString[0])  # add the letter to the location
                shipLocation.append(int(shipLocationString[1:]))  # add the number to the location

                # get the ship's orientation
                print("Placing ship horizontally or vertically (h/v):", end=" ")  # ask for input
                shipOrientation = input().lower()  # get the input

                if self.regexCheck(shipOrientation, "orientation") is False:  # check the input against the regex
                    print("Invalid ship orientation. Orientation should be h or v.")  # print error message
                    input("Please press enter to continue...")  # wait for user to press enter
                    continue  # restart the loop to get the input again when invalid user input is provided

                # Attempt to place the ship after gathering input
                inputValid = self.board.addShip(ship + 1, shipOrientation, shipLocation)
                if not inputValid:  # Only display the error if it exists
                    print(f"{self.board.getErr()}")
                    self.board.clearErr()
                    input("Please press enter to continue...")

    # function used to attack the opponent
    def attack_opponent(self, opponent):
        attackLocation = list()  # Initialize the attack location
        inputValid = False  # Initialize the input variable

        while not inputValid or opponent.board.attack(attackLocation) == False:

            self.cls()  # clear the screen

            # print the attack board and player's board
            print("Attack board:")
            opponent.board.printAttackBoard()  # print the attack board with all previously attacked locations
            print("\n\nYour board:")
            self.board.printBoard()  # print the player's board with all ships placed

            attackLocation.clear()  # clear location

            # check if there was an error
            if opponent.board.getErr() != "":  # if there is an error, print it
                print(f"{opponent.board.getErr()}")
                opponent.board.clearErr()  # clear the error after printing it

            # get the attack location
            print("Enter the location to attack (ex: \"F4\"): ", end=" ")
            attackLocationString = input().upper()

            # check input against regex
            if self.regexCheck(attackLocationString, "location") is False:
                print("Invalid attack location. Location should be [A-J][1-10].")
                input("Please press enter to continue...")
                continue

            # Append the column (letter) to attackLocation
            attackLocation.append(attackLocationString[0])
            attackLocation.append(int(attackLocationString[1:]))

            self.cls()  # clear the screen
            
            # If attack is successful, break out of loop
            if opponent.board.attack(attackLocation):
                inputValid = True  # Attack is valid
                break
            else:
                inputValid = False  # Attack failed, re-enter location

        # show updated attack board
        print("")
        opponent.board.printAttackBoard()  # print the updated attack board
        print("Press enter to continue...", end="")
        input()  # wait for user to press enter

            
    def is_defeated(self):
        return self.board.checkGameOver()  # check if the player is defeated by checking if all ships are sunk


class AIPlayer(Player):
    def __init__(self, name, shipCount, difficulty):
        super().__init__(name, shipCount)
        self.difficulty = difficulty
        self.last_hit = None
        self.possible_targets = []
        self.previous_attacks = set()  # Set to track previously attacked locations

    def place_ships(self):
        # AI randomly places ships automatically
        orientations = ['h', 'v']
        for ship in range(self.shipCount):
            while True:
                shipLocation = [random.choice("ABCDEFGHIJ"), random.randint(1, 10)]
                shipOrientation = random.choice(orientations)
                if self.board.addShip(ship + 1, shipOrientation, shipLocation):
                    break

    def take_turn(self, opponent):
        # AI takes a turn based on difficulty
        if self.difficulty == "easy":
            self.easy_attack(opponent)
        elif self.difficulty == "medium":
            self.medium_attack(opponent)
        elif self.difficulty == "hard":
            self.hard_attack(opponent)
        input()

    def easy_attack(self, opponent):
        attackLocation = [random.choice("ABCDEFGHIJ"), random.randint(1, 10)]

        # Keep selecting a new random location until a valid (non-duplicate) one is found
        while tuple(attackLocation) in self.previous_attacks:
            attackLocation = [random.choice("ABCDEFGHIJ"), random.randint(1, 10)]

        # Record this attack in the list of previous attacks
        self.previous_attacks.add(tuple(attackLocation))

        # Perform the attack and store the result (True = hit, False = miss)
        opponent.board.attack(attackLocation)
        result = opponent.board.hitLocation(attackLocation)

        # Print based on the attack result
        if result:
            print(f"AI hits at {attackLocation[0]}{attackLocation[1]}")
        else:
            print(f"AI misses at {attackLocation[0]}{attackLocation[1]}")


            
    def medium_attack(self, opponent):
        # Medium AI starts randomly, then targets adjacent cells after a hit
        if self.possible_targets:
            attackLocation = self.possible_targets.pop(0)
        else:
            # Random attack if no possible targets left
            attackLocation = [random.choice("ABCDEFGHIJ"), random.randint(1, 10)]

        # Attempt to attack the chosen location
        if opponent.board.attack(attackLocation):
            if opponent.board.hitLocation(attackLocation):
                print(f"AI hits at {attackLocation[0]}{attackLocation[1]}")
                self.last_hit = attackLocation
            else:
                print(f"AI misses at {attackLocation[0]}{attackLocation[1]}")

                self.mark_adjacent(attackLocation, opponent)  # Add adjacent cells
        else:
            print(f"AI misses at {attackLocation[0]}{attackLocation[1]}")
            self.last_hit = None

    def mark_adjacent(self, hit_location, opponent):
        row, col = hit_location
        if col > 1:  # Left
            self.add_target_if_valid([row, col - 1], opponent)
        if col < 10:  # Right
            self.add_target_if_valid([row, col + 1], opponent)
        if row > 'A':  # Up
            self.add_target_if_valid([chr(ord(row) - 1), col], opponent)
        if row < 'J':  # Down
            self.add_target_if_valid([chr(ord(row) + 1), col], opponent)

    def add_target_if_valid(self, location, opponent):
        if not opponent.board.checkDuplicateAttack(location):  # Only add if not already attacked
            self.possible_targets.append(location)
            

    def hard_attack(self, opponent):
        # Hard AI knows exactly where the ships are
        for ship in opponent.board.ships:
            for part in ship.get_coordinates():
                if opponent.board.attack(part):
                    print(f"AI attacks {part[0]}{part[1]}")
                    return
