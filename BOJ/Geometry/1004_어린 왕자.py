import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for i in range(n):
        cx, cy, r = map(int, input().split())
        start = (x1 - cx) ** 2 + (y1 - cy) ** 2
        end = (x2 - cx) ** 2 + (y2 - cy) ** 2
        if start < r ** 2 and end > r ** 2:
            answer += 1
        if end < r ** 2 and start > r ** 2:
            answer += 1
    print(answer)