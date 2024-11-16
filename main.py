import random
import os

# Main function to start the game
def startgame():
    print("Welcome to 2048! Use W, A, S, D to move the tiles up, left, down, and right respectively. Combine tiles to reach 2048!")
    board = [[0] * 4 for _ in range(4)]  # Initialize a 4x4 grid
    board = gennum(board)  # Add the first random number to the board
    gameover = False

    while not gameover:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        printboard(board)  # Display the board
        move = input("Enter your move (W/A/S/D): ").lower()  # Get user input

        # Ensure the input is valid
        while move not in ["w", "a", "s", "d"]:
            move = input("Invalid input! Enter W, A, S, or D: ").lower()

        new_board = [row[:] for row in board]  # Create a copy of the board
        if move == "w":
            new_board = up(board)  # Move tiles up
        elif move == "s":
            new_board = down(board)  # Move tiles down
        elif move == "d":
            new_board = right(board)  # Move tiles right
        elif move == "a":
            new_board = left(board)  # Move tiles left

        # Add a new number if the board changed
        if new_board != board:
            board = gennum(new_board)
        else:
            print("Invalid move!")

        # Check if the game is over
        gameover = checkboard(board)

    print("You Lose!")  # Game over message

# Function to move tiles up
def up(board):
    new_board = [row[:] for row in board]  # Copy the board
    for _ in range(4):  # Repeat to handle merging and shifting
        for row in range(1, 4):
            for column in range(4):
                if new_board[row - 1][column] == 0:  # Move tile up
                    new_board[row - 1][column] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row - 1][column] == new_board[row][column]:  # Merge tiles
                    new_board[row - 1][column] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

# Function to move tiles down
def down(board):
    new_board = [row[:] for row in board]  # Copy the board
    for _ in range(4):  # Repeat to handle merging and shifting
        for row in range(2, -1, -1):
            for column in range(4):
                if new_board[row + 1][column] == 0:  # Move tile down
                    new_board[row + 1][column] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row + 1][column] == new_board[row][column]:  # Merge tiles
                    new_board[row + 1][column] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

# Function to move tiles right
def right(board):
    new_board = [row[:] for row in board]  # Copy the board
    for _ in range(4):  # Repeat to handle merging and shifting
        for column in range(2, -1, -1):
            for row in range(4):
                if new_board[row][column + 1] == 0:  # Move tile right
                    new_board[row][column + 1] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row][column + 1] == new_board[row][column]:  # Merge tiles
                    new_board[row][column + 1] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

# Function to move tiles left
def left(board):
    new_board = [row[:] for row in board]  # Copy the board
    for _ in range(4):  # Repeat to handle merging and shifting
        for column in range(1, 4):
            for row in range(4):
                if new_board[row][column - 1] == 0:  # Move tile left
                    new_board[row][column - 1] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row][column - 1] == new_board[row][column]:  # Merge tiles
                    new_board[row][column - 1] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

# Function to generate a new number on the board
def gennum(board):
    empty_cells = [(row, col) for row in range(4) for col in range(4) if board[row][col] == 0]  # Find empty cells
    if not empty_cells:  # If no empty cells, return the board
        return board
    row, column = random.choice(empty_cells)  # Choose a random empty cell
    board[row][column] = random.choice([2, 4])  # Place a 2 or 4 randomly
    return board

# Function to print the board
def printboard(board):
    print()
    for row in board:
        print(row)  # Print each row of the board

# Function to check if the game is over
def checkboard(board):
    upboard = up(board)  # Simulate an "up" move
    downboard = down(board)  # Simulate a "down" move
    rightboard = right(board)  # Simulate a "right" move
    leftboard = left(board)  # Simulate a "left" move

    # If no moves are possible, the game is over
    if board == upboard and board == downboard and board == rightboard and board == leftboard:
        return True
    else:
        return False

# Start the game
startgame()
