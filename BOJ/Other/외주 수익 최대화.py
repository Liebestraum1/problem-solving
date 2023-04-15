n = int(input())
dp = [0 for _ in range(n+1)] #dp[n] = n일차에 일을 '끝마쳤을 때' 벌 수 있는 돈의 최대값
data = [(0, 0)]

for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))

for i in range(1, n+1): #i는 일을 시작하는 날짜, data[i][0]은 일에 걸리는 시간
    if i + data[i][0] - 1 > n:
        continue
    dp[i + data[i][0] - 1] = max(max(dp[:i + data[i][0]]), data[i][1] + max(dp[:i]))

print(max(dp))