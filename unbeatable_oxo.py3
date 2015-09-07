#!/usr/bin/python3
from copy import deepcopy

PLAYER, COMPUTER = range(2)

def turn():
    if PLAYER == 'O':
        while True:
            yield PLAYER
            yield COMPUTER
    else:
        while True:
            yield COMPUTER
            yield PLAYER

turn = turn()

def is_game_won(matrix):
    if is_oxo_horizontally(matrix):
        return True
    if is_oxo_vertically(matrix):
        return True
    if is_oxo_diagonally(matrix):
        return True
    if is_oxo_cross_diagonally(matrix):
        return True
    return False

def is_game_finished(matrix):
    if (next_move.n >= (len(matrix) * len(matrix[0]))):
        if is_game_won(matrix):
            print("we have a winner!")
        else:
            print("it is a draw")
        return True
    if is_game_won(matrix):
        print("we have a winner!")
        return True
    return False

def score(matrix, player):
    if is_game_won(matrix):
        if player == PLAYER:
            return -10
        else:
            return 10
    else:
        return 0

def generate_moves(matrix):
    moves = list()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == '_':
                moves.append((x,y))
    return moves

def minimax(depth, move, matrix, player):
    matrix[move[0]][move[1]] = player

    if depth == 1 or is_game_won(matrix):
        return depth * score(matrix, player)

    moves = generate_moves(matrix)
    if player == COMPUTER:
        max_val = -10
        for move in moves:
            val = minimax(depth - 1, move, matrix, PLAYER)
            max_val = max(val, max_val)
        return max_val
    else:
        min_val = 10
        for move in moves:
            val = minimax(depth - 1, move, matrix, COMPUTER)
            min_val = min(val, min_val)
        return min_val

def calculate_next_move(matrix):
    max_val = -10
    moves = generate_moves(matrix)
    best_move = moves[0]
    for move in moves:
        new_matrix = deepcopy(matrix)
        val = minimax(len(moves), move, new_matrix, COMPUTER)
        if max_val < val:
            max_val = val
            best_move = move
    return best_move

def wait_for_input(matrix):
    x = int(input("Select row: "))
    y = int(input("Select column: "))
    if x not in range(len(matrix)) or y not in range(len(matrix[0])) or matrix[x][y] != '_':
        print("try again")
        return wait_for_input(matrix)
    return (x,y)

def select_player():
    oorx = input("Select player ['X' or 'O']: ")
    if oorx not in ['X','O']:
        print("try again")
        return select_player()
    return oorx

def next_move(matrix):
    next_move.n += 1
    next_player = next(turn)
    if next_player == PLAYER:
        print("Player's turn:")
        (x, y) = wait_for_input(matrix)
    else:
        print("Computer's turn:")
        (x, y) = calculate_next_move(matrix)

    matrix[x][y] = next_player
    return matrix

def has_oxo_sequence(array):
    for i in range(len(array) - 2):
        if array[i] == 'O' and array[i+1] == 'X' and array[i+2] == 'O':
                return True
    return False

def is_oxo_horizontally(matrix):
    for row in matrix:
        if has_oxo_sequence(row):
            return True
    return False

def is_oxo_vertically(matrix):
    for column in [[row[i] for row in matrix] for i in range(len(matrix[0]))]:
        if has_oxo_sequence(column):
            return True
    return False

def is_oxo_cross_diagonally(matrix):
    for offset in range(-len(matrix[0]),len(matrix)-1):
        diag = [row[-i-1-offset] for i,row in enumerate(matrix) if 0 > -i-1-offset >= -len(row)]
        if has_oxo_sequence(diag):
            return True
    return False

def is_oxo_diagonally(matrix):
    for offset in range(-len(matrix[0]),len(matrix)-1):
        diag = [row[i+offset] for i,row in enumerate(matrix) if 0 <= i+offset < len(row)]
        if has_oxo_sequence(diag):
            return True
    return False

def create_matrix(m, n):
    return [['_' for x in range(n)] for y in range(m)]

def print_matrix(matrix):
    print()
    for row in matrix:
        for val in row:
            print(val, " ", end="")
        print()

if __name__ == "__main__":
    PLAYER = select_player()
    if PLAYER == 'X':
        COMPUTER = 'O'
    else:
        COMPUTER = 'X'
    matrix = create_matrix(3, 3)
    next_move.n = 0
    print_matrix(matrix)
    while (not is_game_finished(matrix)):
        matrix = next_move(matrix)
        print_matrix(matrix)

