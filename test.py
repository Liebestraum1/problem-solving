import sys
input = sys.stdin.readline
n = int(input())
data = []

for _ in range(n):
    a, b = input().split()
    data.append((int(a), b))
    
for i in sorted(data, key=lambda x: x[0]):
    print(*i)