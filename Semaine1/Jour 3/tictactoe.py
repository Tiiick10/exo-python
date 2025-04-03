import sys

def resetBoard():
    
    return {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):

    winningCombos = [
        ['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L']
    ]

    for combo in winningCombos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

while True:

    theBoard = resetBoard()
    turn = 'X'

    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()

        while move not in theBoard or theBoard[move] != ' ':
            print("Already taken. Choose another position:")
            move = input()

        theBoard[move] = turn

        if checkWinner(theBoard, turn):
            printBoard(theBoard)
            print(turn + ' wins!')
            break

        turn = 'O' if turn == 'X' else 'X'

    else:
        printBoard(theBoard)
        print("Draw !")

    again = str(input("Do you want to play again (type yes(y) or no(n)): ")).lower()

    if again != "yes" and again != "y":

        print("Thanks for playing!")

        sys.exit()
