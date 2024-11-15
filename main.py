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
    board[0] = [4,4,2,2] #temp
    board[2] = [8,8,2,4]
    board[3] = [4,4,2,2] #temp
    board[1] = [4,4,2,2]
    printboard(board)

    if move == "w":
        for i in range(0,4):
            for row in range(1,4):
                print("row number: ",row+1)
                for column in range(0,4):
                    if board[row-1][column] == 0:
                        board[row-1][column] = board[row][column]
                        board[row][column] = 0
                    elif board[row-1][column] == board[row][column]:
                        board[row-1][column] += board[row][column]
                        board[row][column] = 0
    
    printboard(board)

        #board[0] = board[3]
    #printboard(board)





def printboard(board):
    print()
    for i in board:
        print(i)




startgame()