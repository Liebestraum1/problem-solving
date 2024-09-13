from collections import deque
from itertools import combinations

n, m = map(int, input().split())

ver = [0, 0, 1, -1]
hor = [1, -1, 0, 0]

board = []
can = []
answer = 0

for row in range(n):
    board.append(list(map(int, input().split())))

for row in range(n):
    for col in range(m):
        if board[row][col] == 0:
            can.append((row, col))

for w1, w2, w3 in combinations(can, 3):
    temp = 0
    aboard = [arr[:] for arr in board]
    aboard[w1[0]][w1[1]], aboard[w2[0]][w2[1]], aboard[w3[0]][w3[1]] = 1, 1, 1
    for row in range(n):
        for col in range(m):
            if aboard[row][col] == 2:
                queue = deque([(row, col)])
                while queue:
                    r, c = queue.popleft()
                    for i in range(4):
                        nr, nc = r + ver[i], c + hor[i]
                        if 0 <= nr < n and 0 <= nc < m and (aboard[nr][nc] == 0 or aboard[nr][nc] == 2):
                            aboard[nr][nc] = 3
                            queue.append((nr, nc))
    for i in range(n):
        for j in range(m):
            if aboard[i][j] == 0:
                temp += 1
    answer = max(temp, answer)

print(answer)