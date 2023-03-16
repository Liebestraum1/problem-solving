import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
array = []
answer = [[0 for col in range(n+1)] for row in range(n+1)]

for _ in range(n):
    array.append(list(map(int, input().split())))

for row in range(1, n+1):
    for col in range(1, n+1):
        answer[row][col] = answer[row][col-1] + array[row-1][col-1]
    for col in range(1, n+1):
        answer[row][col] = answer[row][col] + answer[row-1][col]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(answer[x2][y2] - answer[x1-1][y2] - answer[x2][y1-1] + answer[x1-1][y1-1])