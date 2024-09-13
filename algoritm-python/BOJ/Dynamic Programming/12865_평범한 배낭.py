import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]
item = []
weight_sum = set([0]) #현재까지 나온 값들을 저장할 리스트

for _ in range(n):
    item.append(tuple(map(int, input().split())))

for weight, value in item:
    stack = set()
    dp2 = dp[:]
    for ws in weight_sum:
        if weight + ws > k:
            continue
        dp[weight + ws] = max(dp2[weight + ws], dp2[ws] + value)
        stack.add(weight + ws)
    weight_sum = weight_sum | stack

print(max(dp))