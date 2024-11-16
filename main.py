import random
import os

def startgame():
    print("Welcome to 2048! Use W, A, S, D to move the tiles up, left, down, and right respectively. Combine tiles to reach 2048!")
    board = [[0] * 4 for _ in range(4)]
    board = gennum(board)
    gameover = False

    while not gameover:
        os.system('cls' if os.name == 'nt' else 'clear')
        printboard(board)
        move = input("Enter your move (W/A/S/D): ").lower()

        while move not in ["w", "a", "s", "d"]:
            move = input("Invalid input! Enter W, A, S, or D: ").lower()

        new_board = [row[:] for row in board]  # Create a copy of the board
        if move == "w":
            new_board = up(board)
        elif move == "s":
            new_board = down(board)
        elif move == "d":
            new_board = right(board)
        elif move == "a":
            new_board = left(board)

        if new_board != board:  # Only update if there was a change
            board = gennum(new_board)
        else:
            print("Invalid move!")

        gameover = checkboard(board)

    print("You Lose!")

def up(board):
    new_board = [row[:] for row in board]
    for _ in range(4):
        for row in range(1, 4):
            for column in range(4):
                if new_board[row - 1][column] == 0:
                    new_board[row - 1][column] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row - 1][column] == new_board[row][column]:
                    new_board[row - 1][column] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

def down(board):
    new_board = [row[:] for row in board]
    for _ in range(4):
        for row in range(2, -1, -1):
            for column in range(4):
                if new_board[row + 1][column] == 0:
                    new_board[row + 1][column] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row + 1][column] == new_board[row][column]:
                    new_board[row + 1][column] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

def right(board):
    new_board = [row[:] for row in board]
    for _ in range(4):
        for column in range(2, -1, -1):
            for row in range(4):
                if new_board[row][column + 1] == 0:
                    new_board[row][column + 1] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row][column + 1] == new_board[row][column]:
                    new_board[row][column + 1] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

def left(board):
    new_board = [row[:] for row in board]
    for _ in range(4):
        for column in range(1, 4):
            for row in range(4):
                if new_board[row][column - 1] == 0:
                    new_board[row][column - 1] = new_board[row][column]
                    new_board[row][column] = 0
                elif new_board[row][column - 1] == new_board[row][column]:
                    new_board[row][column - 1] += new_board[row][column]
                    new_board[row][column] = 0
    return new_board

def gennum(board):
    empty_cells = [(row, col) for row in range(4) for col in range(4) if board[row][col] == 0]
    if not empty_cells:
        return board
    row, column = random.choice(empty_cells)
    board[row][column] = random.choice([2, 4])
    return board

def printboard(board):
    print()
    for row in board:
        print(row)

def checkboard(board):
    upboard = up(board)
    downboard = down(board)
    rightboard = right(board)
    leftboard = left(board)

    # Check if all moves leave the board unchanged
    if board == upboard and board == downboard and board == rightboard and board == leftboard:
        return True
    else:
        return False

startgame()
