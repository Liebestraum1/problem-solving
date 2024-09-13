import sys
input = sys.stdin.readline

#sol #1
n = int(input())
pre2, pre1, now = (0, 0), (0, 0), (0, 0) #idx 0은 한 칸, 1은 두 칸 뛴 경우
for _ in range(n):
    pre2, pre1 = pre1, now
    stair = int(input())
    now = (pre1[1] + stair, max(pre2[0], pre2[1]) + stair)
print(max(now))

#sol #2
n = int(input())
data = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(1, n+1):
    data[i] = int(input())

dp[1] = data[1]
dp[2] = dp[1] + data[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3] + data[i] + data[i-1], dp[i-2] + data[i])
print(dp[n])