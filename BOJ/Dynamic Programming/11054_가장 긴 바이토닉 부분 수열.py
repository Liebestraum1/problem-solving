n = int(input())
data1 = list(map(int, input().split()))
data2 = data1[::-1]
dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if data1[j] < data1[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if data2[j] < data2[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2 = dp2[::-1]
dp = [dp1[i] + dp2[i] - 1 for i in range(n)]
print(max(dp))