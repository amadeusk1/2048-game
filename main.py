import random
import os
#os.system('cls' if os.name == 'nt' else 'clear')

def startgame():
    board = []
    for i in range(4):
        board.append([0]*4)  
    board = gennum(board)
    while not (board == left(board) or board == up(board) or board == down(board) or board == right(board)):
        board = gennum(board)
        printboard(board)
        move = input().lower()
        while move not in ["w","a","s","d"]:
            move = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        #board[0] = [4,4,2,2] #temp
        #board[1] = [4,4,2,2]
        #board[2] = [8,8,2,4]
        #board[3] = [4,4,2,2] #temp

        if move == "w":
            board = up(board)    

        elif move == "s":
            board = down(board)

        elif move == "d":
            board = right(board)

        elif move == "a":
            board = left(board)
    print("You Loose")
        
def up(board):
    for i in range(0,4):
            for row in range(1,4):
                for column in range(0,4):
                    if board[row-1][column] == 0:
                        board[row-1][column] = board[row][column]
                        board[row][column] = 0
                    elif board[row-1][column] == board[row][column]:
                        board[row-1][column] += board[row][column]
                        board[row][column] = 0
    return board

def down(board):
    for i in range(0,4):
        for row in range(2,-1,-1):
            for column in range(0,4):
                if board[row+1][column] == 0:
                    board[row+1][column] = board[row][column]
                    board[row][column] = 0
                elif board[row+1][column] == board[row][column]:
                    board[row+1][column] += board[row][column]
                    board[row][column] = 0
    return board

def right(board):
    for i in range(0,4):
        for column in range(2,-1,-1):
            for row in range(0,4):
                    if board[row][column+1] == 0:
                        board[row][column+1] = board[row][column]
                        board[row][column] = 0
                    elif board[row][column+1] == board[row][column]:
                        board[row][column+1] += board[row][column]
                        board[row][column] = 0
    return board

def left(board):
    for i in range(0,4):
        for column in range(3,0):
            for row in range(0,4):
                    if board[row][column-1] == 0:
                        board[row][column-1] = board[row][column]
                        board[row][column] = 0
                    elif board[row][column-1] == board[row][column]:
                        board[row][column-1] += board[row][column]
                        board[row][column] = 0
    return board

def gennum(board):
    row = random.randrange(0,4)
    column = random.randrange(0,4)
    numbergen = random.randrange(2,5,2)
    while board[row][column] > 0:
        row = random.randrange(0,4)
        column = random.randrange(0,4)
        numbergen = random.randrange(2,5,2)
    board[row][column] = numbergen
    return board

def printboard(board):
    print()
    for i in board:
        print(i)




startgame()
