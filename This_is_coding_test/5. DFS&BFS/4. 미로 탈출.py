from collections import deque

n, m = map(int, input().split())
data = []
rm = [-1, 1, 0, 0]
cm = [0, 0, -1, 1]

for _ in range(n):
    data.append(list(map(int, input())))

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            if row + rm[d] >= n or row + rm[d] < 0 or col + cm[d] >= m or col + cm[d] < 0:
                continue
            if data[row + rm[d]][col + cm[d]] == 0:
                continue
            if data[row + rm[d]][col + cm[d]] == 1:
                data[row + rm[d]][col + cm[d]] = data[row][col] + 1
                queue.append((row + rm[d], col + cm[d]))
    return data[n-1][m-1]