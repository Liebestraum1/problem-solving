import sys
input = sys.stdin.readline

data = []
answer = 0
n, m = map(int, input().split())

for _ in range(n):
    data.append(list(map(int, input().rstrip())))

def dfs(row, col):
    if row <= -1 or col <= -1 or col >= m or row >= n:
        return
    if data[row][col] == 0:
        data[row][col] = 1
        dfs(row + 1, col); dfs(row, col + 1)
        dfs(row - 1, col); dfs(row, col - 1)

for row in range(n):
    for col in range(m):
        if data[row][col] == 0:
            answer += 1
            dfs(row, col)

print(answer)