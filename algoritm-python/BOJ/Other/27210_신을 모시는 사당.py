import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data = [1 if i == 1 else -1 for i in data]

s, m, p = 0, 0, 0
for i in data:
    s += i
    if s < 0:
        if s < m:
            m = s
    elif s >= 0:
        s = 0
s = 0
for i in data:
    s += i
    if s > 0:
        if s > p:
            p = s
    elif s <= 0:
        s = 0

print(abs(max(m, p, key=abs)))