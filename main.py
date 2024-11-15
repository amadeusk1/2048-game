import random
import os
#os.system('cls' if os.name == 'nt' else 'clear')

def startgame():
    board = []
    for i in range(4):
        board.append([0]*4)  
    printboard(board)
    '''
    row = random.randrange(0,4)
    column = random.randrange(0,4)
    numbergen = random.randrange(2,5,2)
    board[row][column] = numbergen
    printboard(board)
    '''
    printboard(board)
    move = input().lower()
    while move not in ["w","a","s","d"]:
        move = input()
    board[3] = [4,4,2,2]
    printboard(board)
    if move == "w":
        board[0] = board[3]
    printboard(board)





def printboard(board):
    print()
    for i in board:
        print(i)




startgame()