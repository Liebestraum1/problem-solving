import sys
input = sys.stdin.readline

n = int(input())
data = []
dp = [1 for _ in range(n)]

for _ in range(n):
    data.append(tuple(map(int, input().split())))

v = [i[1] for i in sorted(data, key = lambda x: x[0])]

for i in range(1, n):
    for j in range(i):
        if v[j] < v[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))