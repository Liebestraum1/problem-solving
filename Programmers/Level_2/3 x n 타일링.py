def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[2] = 1, 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2]
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j] * 2
        dp[i] = (dp[i]) % 1000000007 
    return dp[-1]