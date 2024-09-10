"""
Name: board.py
Description: This is the board class, information to be added later
Authors: Carson Treece, Zachary Craig
Other Sources: ...
Date Created: 9/9/2024
Last Modified: 9/9/2024
"""

import copy

class Board:
    def __init__(self, shipCount):
        self.boardSize = 10 # define the board size to 10
        self.board = self.createBoard(10) # creates the board
        self.ships = [] # initialize the list of ships
        self.shipCount = shipCount # define the number of ships
    
    # creates the board
    def createBoard(self, boardSize):
        board = [["~" for i in range(boardSize)] for j in range(boardSize)] # create the board using ~ for empty spaces
        return board

    # print the board
    def printBoard(self):        
        print("   A B C D E F G H I J\n") # print the column labels
        for i in range(self.boardSize): # for each row
            if(i < 9):
                print(i+1 , end="  ") # print the row label with two spaces to accomodate the 10th row label
            else:
                print(i+1 , end=" ") # print the row label with one space because it is a two digit number
            for j in range(self.boardSize): # for each column
                print(self.board[i][j], end=" ") # print the value of the board at that location
            print() # print a new line after each row
    
    # check if the ship collides with another ship
    def checkShipCollision(self, newBoard, oldBoard):
        for i in range(self.boardSize): # for each row
            for j in range(self.boardSize): # for each column
                if(newBoard[i][j] != "~" and oldBoard[i][j] != "~"): # if the location is not empty on both the new and old board
                    return True # return that there is a collision
        return False # return that there is no collision
    
    # column label to number
    def columnLabelToNumber(self, columnLabel):
        columnLabel = columnLabel.lower() # convert the column label to lowercase
        num = ord(columnLabel) - 96 # converts the lowercase column letter to its unicode value and subtracts 96 to get the column number
        return num

    # check if the ship collides with the edge of the board
    def checkBoardCollision(self, shipSize, shipOrientation, shipLocation):
        if(shipOrientation == "v"): # checks if the ship is vertical
            if(shipLocation[1] + shipSize - 1 > self.boardSize): # checks if the ship head location plus the size of the ship is greater than the board size
                return True
        elif(shipOrientation == "h"): # checks if the ship is horizontal
            if(self.columnLabelToNumber(shipLocation[0]) + shipSize - 1 > self.boardSize): # checks if the ship head location plus the size of the ship is greater than the board size
                return True
        return False
    
    # add a ship to the board
    def addShip(self, shipSize, shipOrientation, shipLocation):
        # creates a new array for the ship to reference against the current board
        tempBoard = self.createBoard(self.boardSize)
        
        
        # check if the ship is vertical
        if shipOrientation == "v":
            # check if the ship collides with the edge of the board
            if(self.checkBoardCollision(shipSize, shipOrientation, shipLocation)):
                print("Ship collides with the edge of the board. Please place the ship in a different location.")
                return False
            # add the ship to the tempBoard
            for i in range(shipSize): # for each part of the ship
                tempBoard[shipLocation[1]+i-1][self.columnLabelToNumber(shipLocation[0])-1] = shipSize # add the ship's part to the tempBoard
            
        # check if the ship is horizontal
        elif shipOrientation == "h":
            # check if the ship collides with the edge of the board
            if(self.checkBoardCollision(shipSize, shipOrientation, shipLocation)):
                print("Ship collides with the edge of the board. Please place the ship in a different location.")
                return False
            # add the ship to the tempBoard
            for i in range(shipSize): # for each part of the ship
                tempBoard[shipLocation[1]-1][self.columnLabelToNumber(shipLocation[0])+i-1] = shipSize # add the ship's part to the tempBoard
            
        # check if the ship collides with another ship
        if(self.checkShipCollision(self.board, tempBoard)):
            print("Ship collides with another ship. Please place the ship in a different location.")
            return False
        
        # after checking for collisions, concatenate update board
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if(tempBoard[i][j] != "~"):
                    self.board[i][j] = tempBoard[i][j]
        
        # add the ship to the list of ships
        self.ships.append(shipSize)
    
    
    
    # Remove before production
    def printShips(self):
        print(self.ships)
    


# Test code

player1Board = Board(5)
player1Board.addShip(1, "h", ["A", 1])
player1Board.addShip(2, "h", ["A", 2])
player1Board.addShip(3, "h", ["A", 3])
player1Board.addShip(4, "h", ["A", 4])
# player1Board.addShip(4, "v", ["E", 1])
player1Board.addShip(5, "h", ["A", 5])
player1Board.printBoard()
player1Board.printShips()
