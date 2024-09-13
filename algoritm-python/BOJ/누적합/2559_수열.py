n, k = map(int, input().split())
data = list(map(int, input().split()))
answer = [0, data[0]]
result = -100000001

for i in range(1, n):
    answer.append(answer[-1] + data[i])

for i in range(k, n+2):
    if result < answer[i] - answer[i-k]:
        result = answer[i] - answer[i-k]

print(result)