import random

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, row, col):
    # Проверка строки
    if num in board[row]:
        return False
    
    # Проверка столбца
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Проверка 3x3 квадрата
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if valid(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0
    
    return False

def generate_board():
    base = 3
    side = base * base
    nums = random.sample(range(1, base*base + 1), base*base)
    board = [[0]*side for _ in range(side)]
    
    for i in range(base):
        for j in range(base):
            for k in range(base):
                board[i * base + j][(i + k) % base * base + (j + k) % base] = nums[(i * base + j + k) % (base * base)]
    
    return board

# Инициализация головоломки Судоку
sudoku_board = generate_board()
print("Сгенерированная Судоку:")
print_board(sudoku_board)

if solve(sudoku_board):
    print("\nРешение Судоку:")
    print_board(sudoku_board)
else:
    print("Нет решения для данной Судоку.")