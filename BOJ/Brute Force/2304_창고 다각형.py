n = int(input())

high_l, high_h = 0, 0 #위치, 높이
data = []
stack = 0
answer = 0

for _ in range(n):
    data.append(tuple(map(int, input().split())))


for l, h in enumerate(sorted(data, key = lambda x: x[0])):
    if h > high_h:
        answer += (l - high_l) * h
        l, h = high_l, high_h
    elif idx == n-1:
        answer += max(data[l:]) * (n - l - 1)

print(answer)