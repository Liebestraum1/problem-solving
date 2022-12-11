#Programmer lv.2, [1차] 프렌즈 4블록
def solution(m, n, board):
    for i, v in enumerate(board):
        board[i] = list(v)
    
    stack = ['0']
    answer = 0
    while stack:
        stack = []
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] != '0' and board[row][col] == board[row][col+1] and board[row][col+1] == board[row+1][col] and board[row+1][col] == board[row+1][col+1]:
                    stack += [(row, col), (row+1, col), (row, col+1), (row+1, col+1)]

        for i, v in stack:
            board[i][v] = '0' 

        for y in range(n):
            x = 0
            while x < m-1:
                if board[x][y] != '0':
                    if board[x+1][y] == '0':
                        board[x+1][y] = board[x][y]
                        board[x][y] = '0'
                        x = -1
                x += 1
    for cnt in board:
        answer += cnt.count('0')
    return answer