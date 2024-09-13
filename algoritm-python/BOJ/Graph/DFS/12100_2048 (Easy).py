n = int(input())
board = []
answer = []
dr = ["UP", "DOWN", "RIGHT", "LEFT"]

def moving(direction, board):
    nboard = [[0 for col in range(n)] for row in range(n)]
    if direction == "UP":
        for col in range(n):
            idx, merged = -1, False
            for row in range(n):
                if board[row][col] != 0:
                    if board[row][col] == nboard[idx][col] and not merged:
                        merged = True
                        nboard[idx][col] += board[row][col]
                    else:
                        merged = False
                        idx += 1
                        nboard[idx][col] += board[row][col]
    if direction == "DOWN":
        for col in range(n):
            idx, merged = 0, False
            for row in range(n-1, -1, -1):
                if board[row][col] != 0:
                    if board[row][col] == nboard[idx][col] and not merged:
                        merged = True
                        nboard[idx][col] += board[row][col]
                    else:
                        merged = False
                        idx -= 1
                        nboard[idx][col] += board[row][col]
    if direction == "LEFT":
        for row in range(n):
            idx, merged = -1, False
            for col in range(n):
                if board[row][col] != 0:
                    if board[row][col] == nboard[row][idx] and not merged:
                        merged = True
                        nboard[row][idx] += board[row][col]
                    else:
                        merged = False
                        idx += 1
                        nboard[row][idx] += board[row][col]
    if direction == "RIGHT":
        for row in range(n):
            idx, merged = 0, False
            for col in range(n-1, -1, -1):
                if board[row][col] != 0:
                    if board[row][col] == nboard[row][idx] and not merged:
                        merged = True
                        nboard[row][idx] += board[row][col]
                    else:
                        merged = False
                        idx -= 1
                        nboard[row][idx] += board[row][col]
    return nboard

def dfs(board, depth):
    if depth == 5:
        answer.append(max(map(max, board)))
        return
    for d in dr:
        dfs(moving(d, board), depth+1)

for row in range(n):
    board.append(list(map(int, input().split())))

dfs(board, 0)
print(max(answer))