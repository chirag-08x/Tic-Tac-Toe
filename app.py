import random

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ]

def printBoard():
    for i in board:
        print(i)
    print("")

def playTicTacToe():
    i = 1
    entries = [0, 1]
    while i <= 9:
        randomRow = random.randint(0, 2)
        randomCol = random.randint(0, 2)
        if board[randomRow][randomCol] != 0:
            continue
        if(i % 2 == 0):
            board[randomRow][randomCol] = 1
        else:
            board[randomRow][randomCol] = 2
            
        i += 1
        printBoard()
        winner = checkForWinner()
        if(winner):
            return
    print("Match has drawn.")

def checkForWinner():
    for item in board:
        check = item[0] == item[1] == item[2] and item[0] == item[1] == item[2] != 0
        if check:
            print(f"Player {item[0]} has won.")
            return True

    for item in range(len(board)):
        check = board[0][item] == board[1][item] == board[2][item] and board[0][item] == board[1][item] == board[2][item] != 0
        if check:
            print(f"Player {board[0][item]} has won.")
            return True
    return False

playTicTacToe()
