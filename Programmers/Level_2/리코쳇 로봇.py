from collections import deque
def solution(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'R':
                start = (row, col, 0)
            if board[row][col] == 'G':
                goal = (row, col)
    
    dr = [1, -1, 0, 0] #아래, 위
    dc = [0, 0, 1, -1] #오른쪽, 왼쪽
    
    visited = {start[:2]}
    queue = deque([start])
    while queue:
        row, col, score = queue.popleft()
        if (row, col) == goal:
            return score
        for i in range(4):
            nr, nc = row, col
            while nr + dr[i] >= 0 and nr + dr[i] <= len(board) - 1 and nc + dc[i] >= 0 and nc + dc[i] <= len(board[0]) - 1 and board[nr + dr[i]][nc + dc[i]] != 'D':
                nr, nc = nr + dr[i], nc + dc[i]
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, score + 1))
    return -1