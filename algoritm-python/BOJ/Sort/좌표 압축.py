import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

dic = {}
for i, v in enumerate(sorted(list(set(data)))):
    dic[v] = i

for key in data:
    print(dic[key], end=' ')