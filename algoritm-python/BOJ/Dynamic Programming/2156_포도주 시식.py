import sys
input = sys.stdin.readline
n = int(input())

dp = [0]
s = [0]

for i in range(1, n+1):
    s.append(int(input()))
    if i < 3:
        dp.append(s[i-1] + s[i])
    else:
        dp.append(max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i], dp[i-1]))

print(dp[-1])