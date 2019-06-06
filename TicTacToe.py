# Tic-tac-toe game
# author: Sooyong Lee

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkWinner(board):
    return ((board['1'] == board['2'] == board['3'] and board['1'] != ' ') or
    (board['4'] == board['5'] == board['6'] and board['4'] != ' ') or
    (board['7'] == board['8'] == board['9'] and board['7'] != ' ') or
    (board['1'] == board['4'] == board['7'] and board['1'] != ' ') or
    (board['2'] == board['5'] == board['8'] and board['2'] != ' ') or
    (board['3'] == board['6'] == board['9'] and board['3'] != ' ') or
    (board['1'] == board['5'] == board['9'] and board['1'] != ' ') or
    (board['3'] == board['5'] == board['7'] and board['3'] != ' '))


turn = 'X'
won = False
while not won:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if theBoard[move] == ' ':
        theBoard[move] = turn
    else:
        print('Enter a valid space.')
        continue
    if checkWinner(theBoard):
        printBoard(theBoard)
        print('The winner is: ' + turn + "!")
        won = True
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'