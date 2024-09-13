n = int(input())
dp = [[0] * 10 for _ in range(n)]

dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i-1][k+1]
        elif k == 9:
            dp[i][k] = dp[i-1][k-1]
        else:
            dp[i][k] = dp[i-1][k+1] + dp[i-1][k-1]
print(sum(dp[-1][1:])%1000000000)