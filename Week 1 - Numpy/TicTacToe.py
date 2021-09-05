import numpy as np

size = int(input('Size of board (n x n): '))
board = np.full((size, size), "  ")
print(board)


def player(num):
    row = int(input('Player {} '.format(num)))
    col = int(input('Player {} '.format(num)))
    
    # Xét xem vị trí vừa nhập có trùng hay ko, nếu trùng cho nhập lại
    while board[row, col] == 'x' or board[row, col] == 'o':
        row = int(input('Occupied. Try again!'))
        col = int(input('Occupied. Try again!'))
        
    if board[row, col] == '  ':
        if num == 1:
            board[row, col] = 'x'
        elif num == 2:
            board[row, col] = 'o'
    print(board)
    

def win_condition(arr):
    n = board.shape[0]
    # Check xem row đang xét full x hay full o
    for i in range(n):
        if len(set(board[i])) == 1:
            if 'x' in board[i]:
                return 1
            elif 'o' in board[i]:
                return 2
            
    # Check xem col đang xét full x hay full o
    for j in range(n):
        if len(set(board[:, j])) == 1:
            if 'x' in board[:, j]:
                return 1
            elif 'o' in board[:, j]:
                return 2
            
    if len(set(board.diagonal())) == 1:
        if 'x' in board.diagonal():
            return 1
        elif 'o' in board.diagonal():
            return 2
    if len(set(np.fliplr(board).diagonal())) == 1:
        if 'x' in np.fliplr(board).diagonal():
            return 1
        elif 'o' in np.fliplr(board).diagonal():
            return 2
    if '_' not in board:
        return 3

# Check kết quả trận đấu
while '_' in board:
    player(1)
    if win_condition(board) == 1:
        print('Player 1 wins')
        break
    if win_condition(board) == 3:
        print('Draw')
        break

    player(2)
    if win_condition(board) == 2:
        print('Player 2 wins')
        break
    if win_condition(board) == 3:
        print('Draw')
        break




