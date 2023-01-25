import sys
input = sys.stdin.readline
n, m = map(int, input().split())

answer = 0
data = set()
for _ in range(n):
    data.add(input())

for _ in range(m):
    if input() in data:
        answer += 1

print(answer)