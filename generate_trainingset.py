import json
import random

dataset = []

def generate_board(rows, columns):
    board = []
    for i in range(rows):
        row = [None] * columns
        board.append(row)
    return board

def generate_random(board):
    for row in board:
        for column in row:
            column = random.choice([None,1,2])
    return board

def new_line_horizontal(board, colour):
    row = random.randint(0, len(board) - 1)
    column = random.randint(0, len(board[0]) - 4)
    for i in range(4):
        board[row][column + i] = colour
    return board

def new_line_vertical(board, colour):
    row = random.randint(0, len(board) - 4)
    column = random.randint(0, len(board[0]) - 1)
    for i in range(4):
        board[row + i][column] = colour
    return board

def new_line_diagonal_right(board, colour):
    row = random.randint(0, len(board) - 4)
    column = random.randint(0, len(board[0]) - 4)
    for i in range(4):
        board[row + i][column + i] = colour
    return board

def new_line_diagonal_left(board, colour):
    row = random.randint(0, len(board) - 4)
    column = random.randint(3, len(board[0]) - 1)
    for i in range(4):
        board[row + i][column - i] = colour
    return board

def board_choice():
    win = random.choice([True, False])
    type = False
    if win:
        type = random([new_line_diagonal_left, new_line_diagonal_right, new_line_horizontal, new_line_vertical])
    return type

def generate_pair():
    board = generate_board(6, 7)
    board = generate_random(board)
    colour = random.choice([None,0,0,1,1])
    type = board_choice()
    if type and colour:
        board = type(board, colour)
    set = {}
    set['board'] = board
    set['colour'] = colour
    return set


    
    

