"""
Name: board.py
Description: This is the board class, information to be added later
Authors: Carson Treece, Zachary Craig, Joshua Park
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/12/2024
"""

import copy
from ship import Ship
import re

class Board:
    def __init__(self, shipCount):
        self.boardSize = 10  # define the board size to 10
        self.board = self.createBoard(10)  # creates the board
        self.attackBoard = self.createBoard(10)  # creates the attack board
        self.ships = list()  # initialize the list of ships
        self.shipCount = shipCount  # define the number of ships
        self.err = ""  # initialize the error message
        
    # function to get the last error message
    def getErr(self):
        return self.err
    
    # function to clear the error message
    def clearErr(self):
        self.err = ""
    
    # creates the board
    def createBoard(self, boardSize):
        board = [["~" for i in range(boardSize)] for j in range(boardSize)]  # create the board using ~ for empty spaces
        return board

    # print the board
    def printBoard(self):        
        print("   A B C D E F G H I J")  # print the column labels
        for i in range(self.boardSize):  # for each row
            if i < 9:
                print(i+1 , end="  ")  # print the row label with two spaces to accommodate the 10th row label
            else:
                print(i+1 , end=" ")  # print the row label with one space because it is a two-digit number
            for j in range(self.boardSize):  # for each column
                print(self.board[i][j], end=" ")  # print the value of the board at that location
            print()  # print a new line after each row
    
    # check if the ship collides with another ship
    def checkShipCollision(self, newBoard, oldBoard):
        for i in range(self.boardSize):  # for each row
            for j in range(self.boardSize):  # for each column
                if newBoard[i][j] != "~" and oldBoard[i][j] != "~":  # if the location is not empty on both the new and old board
                    return True  # return that there is a collision
        return False  # return that there is no collision
    
    # column label to number
    def columnLabelToNumber(self, columnLabel):
        return ord(columnLabel.lower()) - 96  # converts the lowercase column letter to its Unicode value and subtracts 96 to get the column number

    # check if the ship collides with the edge of the board
    def checkBoardCollision(self, shipSize, shipOrientation, shipLocation):
        if shipOrientation == "v":  # checks if the ship is vertical
            if shipLocation[1] + shipSize - 1 > self.boardSize:  # checks if the ship head location plus the size of the ship is greater than the board size
                return True
        elif shipOrientation == "h":  # checks if the ship is horizontal
            if self.columnLabelToNumber(shipLocation[0]) + shipSize - 1 > self.boardSize:  # checks if the ship head location plus the size of the ship is greater than the board size
                return True
        return False
    
    # add a ship to the board
    def addShip(self, shipSize, shipOrientation, shipLocation):
        # creates a new array for the ship to reference against the current board
        tempBoard = self.createBoard(self.boardSize)
        
        # check if the ship is vertical
        if shipOrientation == "v":
            # check if the ship collides with the edge of the board
            if self.checkBoardCollision(shipSize, shipOrientation, shipLocation):
                self.err = "Ship collides with the edge of the board. Please place the ship in a different location."  # set the error message for board collision
                return False
            # add the ship to the tempBoard
            for i in range(shipSize):  # for each part of the ship
                tempBoard[shipLocation[1]+i-1][self.columnLabelToNumber(shipLocation[0])-1] = shipSize  # add the ship's part to the tempBoard
            
        # check if the ship is horizontal
        elif shipOrientation == "h":
            # check if the ship collides with the edge of the board
            if self.checkBoardCollision(shipSize, shipOrientation, shipLocation):  # check if the ship collides with the edge of the board
                self.err = "Ship collides with the edge of the board. Please place the ship in a different location."  # set the error message for board collision
                return False
            # add the ship to the tempBoard
            for i in range(shipSize):  # for each part of the ship
                tempBoard[shipLocation[1]-1][self.columnLabelToNumber(shipLocation[0])+i-1] = shipSize  # add the ship's part to the tempBoard
            
        # check if the ship collides with another ship
        if self.checkShipCollision(self.board, tempBoard):
            self.err = "Ship collides with another ship. Please place the ship in a different location."  # set the error message for ship collision
            return False
        
        # after checking for collisions, concatenate update board
        for i in range(self.boardSize):  # for each row
            for j in range(self.boardSize):  # for each column
                if tempBoard[i][j] != "~":  # if the location is not empty on the tempBoard
                    self.board[i][j] = tempBoard[i][j]  # update the board with the ship's part
        
        ship = Ship(shipSize, shipOrientation, shipLocation)  # create a new ship object with the ship's size, orientation, and location
        self.ships.append(ship)  # add the ship to the list of ships
        
        return True  # return that the ship has been successfully added to the board
    
    # check if a ship has been hit
    def checkHit(self, missileLocation):
        if re.match("^[HSM~]$", str(self.board[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1])):  # checks value at board against regex expression to match "H" or "S" or "M" or "~"
            return False  # return that the attack is a hit
        return True  # return that the attack is a miss
    
    # check if a ship has been sunk
    def checkSunk(self, ship):
        if self.ships[ship].is_sunk():  # if the ship is sunk
            for i in range(self.ships[ship].getSize()):  # for each part of the ship
                if self.ships[ship].getOrientation() == "v":  # if the ship is vertical
                    self.board[self.ships[ship].getLocation()[1]+i-1][self.columnLabelToNumber(self.ships[ship].getLocation()[0])-1] = "S"  # update the board with a S for each part to signify a sunk ship
                elif self.ships[ship].getOrientation() == "h":  # if the ship is horizontal
                    self.board[self.ships[ship].getLocation()[1]-1][self.columnLabelToNumber(self.ships[ship].getLocation()[0])+i-1] = "S"  # update the board with a S for each part to signify a sunk ship
            return True  # return that the ship is sunk
        return False  # return that the ship is not sunk
    
    # method to initiate an attack
    # returns true if the attack action was successful
    # returns false if the attack was a duplicate to allow the player to choose a different location
    def attack(self, missileLocation):        
        if self.checkDuplicateAttack(missileLocation):  # check if the attack is a duplicate
            self.err = "Duplicate attack! Please choose a different location."  # set the error message for duplicate attack
            return False  # return that the attack is a duplicate
        
        if self.checkHit(missileLocation):  # check if the attack is a hit
            damagedShip = self.board[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1]-1  # get the damaged ship
            self.board[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1] = "H"  # update the board with a hit
            
            self.ships[damagedShip].hit()  # add a hit to the ship
            if self.checkSunk(damagedShip):  # check if the ship is sunk
                print("Ship sunk!")  # print that the ship is sunk
            else:  # if the ship is not sunk
                print("Hit!")  # print that the attack is a hit
            
            self.attackBoard[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1] = "H"  # update the attack board with a hit
            
        else:  # if the attack is a miss
            self.board[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1] = "M"  # update the board with a miss
            print("Miss!")  # print that the attack is a miss
            
            self.attackBoard[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1] = "M"  # update the attack board with a miss

        return True  # return that the attack action was successful
            
    # check if duplicate attack
    def checkDuplicateAttack(self, missileLocation):
        if re.match("^[HSM]$", str(self.attackBoard[missileLocation[1]-1][self.columnLabelToNumber(missileLocation[0])-1])):  # checks value at board against regex expression to match "H" or "S" or "M"
            return True  # return that the attack is a hit
        return False  # return that the attack is not a duplicate
        
    # method to check if all ships have been sunk
    def checkGameOver(self):
        for ship in self.ships:  # for each ship
            if not ship.is_sunk():  # if the ship is not sunk
                return False  # return that the game is not over if there is at least one ship that is not sunk
        return True  # return that the game is over if all ships are sunk
    
    # method to print the attack board
    # this board keeps track of the attacks made by the player on the opponent's board
    def printAttackBoard(self):
        print("   A B C D E F G H I J\n")  # print the column labels
        for i in range(self.boardSize):  # for each row
            if i < 9:
                print(i+1 , end="  ")  # print the row label with two spaces to accommodate the 10th row label
            else:
                print(i+1 , end=" ")  # print the row label with one space because it is a two-digit number
            for j in range(self.boardSize):  # for each column
                print(self.attackBoard[i][j], end=" ")
            print()  # print a new line after each row
