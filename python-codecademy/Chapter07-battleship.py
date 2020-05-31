'''Simplified, one-player version of the classic board game
Battleship! In this version of the game, there will be a
single ship hidden in a random location on a 5x5 grid.
The player will have 10 guesses to try to sink the ship.'''

# Functions used: .join, input, generate random int, print using f-string

# Use .join method to print the board
from random import randint

board = []
for n in range(5):
    board.append(['O', 'O', 'O', 'O', 'O'])


def print_board(board_in):
    for row in board_in:
        print(" ".join(row))


print_board(board)


# Generate random_row and random_col -
# location of the battleship on the board

def random_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(f'ship_row: {ship_row}')
print(f"ship_col: {ship_col}")

# Guess row and col

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

# Check the guess

if guess_row == ship_row and guess_col == ship_col:
    print(f"Congratulations! You sank my battleship!")
