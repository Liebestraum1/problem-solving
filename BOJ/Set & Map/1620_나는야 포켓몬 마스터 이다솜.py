import sys
input = sys.stdin.readline
dic = {}
n, m = map(int, input().split())
for i in range(1, n+1):
    p = input().rstrip()
    dic[p], dic[i] = i, p

for _ in range(m):
    d = input().rstrip()
    if d.isdigit():
        print(dic[int(d)])
    else:
        print(dic[d])