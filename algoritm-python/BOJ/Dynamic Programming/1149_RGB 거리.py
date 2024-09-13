import sys
input = sys.stdin.readline
n = int(input())

data = [[0, 0, 0] for _ in range(n+1)]

for row in range(1, n+1):
    r, g, b = map(int, input().split())
    data[row][0] = r + min(data[row-1][1], data[row-1][2])
    data[row][1] = g + min(data[row-1][0], data[row-1][2])
    data[row][2] = b + min(data[row-1][0], data[row-1][1])

print(min(data[-1]))