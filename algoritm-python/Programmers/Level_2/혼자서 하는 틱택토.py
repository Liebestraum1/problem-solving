def solution(board):
    def f(char: str):
        for row in board:
            if row == char * 3:
                return True
        for col in zip(*board):
            if col == (char, char, char):
                return True
        if board[0][0] + board[1][1] + board[2][2] == char * 3:
            return True
        if board[0][2] + board[1][1] + board[2][0] == char * 3:
            return True
        return False
    
    cnt_o, cnt_x = 0, 0
    for row in board:
        for col in row:
            if col == 'O':
                cnt_o += 1
            if col == 'X':
                cnt_x += 1
    
    if cnt_o - cnt_x == 1:
        if f('X'):
            return 0
        else:
            return 1
    elif cnt_o - cnt_x == 0:
        if f('O'):
            return 0
        else:
            return 1
    else:
        return 0