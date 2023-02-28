n, m = map(int, input().split())
data = list(map(int, input().split()))

prefix_sum = [data[0]%m]
remainder = [0 for _ in range(m)]
answer = 0

for i in data[1:]:
    prefix_sum.append((prefix_sum[-1] + i) % m)

for i in prefix_sum:
    if i == 0:
        remainder[i] += 1
        answer += remainder[0]
    else:
        answer += remainder[i]
        remainder[i] += 1

print(answer)