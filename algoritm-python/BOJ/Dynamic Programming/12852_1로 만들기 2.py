n = int(input())
dp = [0 for _ in range(n+1)]
p = [1] + [0 for _ in range(n)]
idx = n

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    p[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        p[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        p[i] = i // 3

print(dp[n])
for _ in range(dp[n] + 1):
    print(idx, end=' ')
    idx = p[idx]