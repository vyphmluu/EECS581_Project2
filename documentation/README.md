# EECS581_Project1
Repositiory for EECS 581 Team 27

This respository contains our code for **Project 1** of **EECS 581**, the game **Battleship**. We decided to implement the game as a Python CLI application. The following is a breakdown of the structure and flow of our program.

## Files

### `ship.py`
Contains the `Ship` class, which tracks the size, number of hits, orientation, and location of a ship.

### `player.py`
Contains the `Player` class, which tracks the name, board, and number of ships associated with each player. It contains methods that 
- process input from the players
- allow the players to place ships on their boards and attack their opponent
- check if a player has been defeated

### `board.py`
Contains the `Board` class, which actually consists of two boards:
  - The `board`, which is used to track the opponent's attacks (hits and misses) on a player's ships.
  - The `attackBoard`, which is used to track a player's attacks on the opponent.

It contains a list of the ships that have been placed on the board. It also contains methods that
- print the boards
- ensure valid ship placements
- add ships to the board
- check if a ship has been hit or sunk
- update the boards with the result of an attack
- check if all ships have been sunk

### `battleship.py`
Creates the necessary instances of the classes described above. It contains the main loop of the game.

## Game Loop

The game consists of the following steps:

1. Get the number of ships from each player.
2. Create an instance of the `Player` class for each of the two players.
3. Allow each player to place their ships on their boards.

Then, these steps loop:

1. Let **Player 1** attack **Player 2**.
2. Check if **Player 2** is defeated. If yes, then end the game.
3. Let **Player 2** attack **Player 1**.
4. Check if **Player 1** is defeated. If yes, then end the game.
