n = int(input())
board = []
answer = []
dr = ["UP", "DOWN", "RIGHT", "LEFT"]

def moving(direction, board):
    if direction == "UP":
        for col in range(n):
            for row in range(n-1, 0, -1):
                if board[row][col] != 0 and board[row-1][col] == 0:
                    board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
                elif board[row][col] != 0 and board[row][col] == board[row-1][col]:
                    board[row][col], board[row-1][col] = board[row][col] * 2, 0

    if direction == "DOWN":
        for col in range(n):
            for row in range(n-1):
                if board[row][col] != 0 and board[row+1][col] == 0:
                    board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
                elif board[row][col] != 0 and board[row][col] == board[row+1][col]:
                    board[row][col], board[row+1][col] = board[row][col] * 2, 0
    if direction == 'LEFT':
        for row in range(n):
            for col in range(n-1, 0, -1):
                if board[row][col] != 0 and board[row][col-1] == 0:
                    board[row][col], board[row][col-1] = board[row][col-1], board[row][col]
                elif board[row][col] != 0 and board[row][col] == board[row][col-1]:
                    board[row][col], board[row][col-1] = board[row][col] * 2, 0
    if direction == 'RIGHT':
        for row in range(n):
            for col in range(n-1):
                if board[row][col] != 0 and board[row][col-1] == 0:
                    board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
                elif board[row][col] != 0 and board[row][col] == board[row][col+1]:
                    board[row][col], board[row][col+1] = board[row][col] * 2, 0
    return board

def dfs(board, depth, a):
    if depth == 1:
        answer.append(max(map(max, board)))
        print(a)
        print(*board, sep='\n')
        print('절취선')
        return
    for d in dr:
        dfs(moving(d, board), depth+1, d)

for row in range(n):
    board.append(list(map(int, input().split())))

dfs(board, 0, 'UP')
print(max(answer))