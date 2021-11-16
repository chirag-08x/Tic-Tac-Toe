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
    leftDiagnol = set()
    rightDiagnol = set()

    for index,item in enumerate(board):
        # Check for similar number in rows.
        rowItems = {item[0], item[1], item[2]}
        check = len(rowItems) == 1 and 0 not in rowItems
        if check:
            print(f"Player {item[0]} has won.")
            return True

        # checking for similar number in columns.
        colItems = {board[0][index], board[1][index],board[2][index]}
        check = len(colItems) == 1 and 0 not in colItems
        if check:
            print(f"Player {board[0][index]} has won.")
          
            return True
        # Adding diagnol element to the set.
        for i in range(len(board)):
            leftDiagnol.add(board[i][i])
            rightDiagnol.add(board[i][len(board) - 1 - i])

    # checking for diagnols
    if len(leftDiagnol) == 1 and 0 not in leftDiagnol:
        print(f"Player {board[1][1]} has won the game.")
        return True
    
    # checking for diagnols
    if len(rightDiagnol) == 1 and 0 not in rightDiagnol:
        print(f"Player {board[1][1]} has won the game.")
        return True

    return False

playTicTacToe()