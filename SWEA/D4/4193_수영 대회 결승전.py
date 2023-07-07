t = int(input())

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

def dfs(row, col, time):
    global n, c, d, drow, dcol
    if time >= visited[row][col]:
        return
    visited[row][col] = time
    if row == c and col == d:
        return
    for move in range(3):
        mrow, mcol = row + drow[move], col + dcol[move]
        if mrow < 0 or mcol < 0 or mrow >= n or mcol >= n or board[mrow][mcol] == 1:
            continue
        elif board[mrow][mcol] == 0:
            dfs(mrow, mcol, time + 1)
        else:
            dfs(mrow, mcol, time + 3 - time % 3)

for case in range(1, t + 1):
    n = int(input())
    board = []
    visited = [[999 for i in range(n)] for j in range(n)]
    for row in range(n):
        board.append(list(map(int, input().split())))
    
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    dfs(a, b, 0)

    print(f"#{case} {visited[c][d]}")