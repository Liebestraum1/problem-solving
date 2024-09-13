t = int(input())
for case in range(t):
    n = int(input())
    dp = [[0 for _ in range(n+1)] for row in range(2)]
    data = []
    for row in range(2):
        data.append(list(map(int, input().split())))
    
    dp[0][1], dp[1][1] = data[0][0], data[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + data[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + data[1][i-1]
    print(max(dp[1][n], dp[0][n]))