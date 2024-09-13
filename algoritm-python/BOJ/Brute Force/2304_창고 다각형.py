n = int(input())

high_l, high_h = 0, 0 #위치, 높이
data = []
stack = []
answer = 0

for _ in range(n):
    data.append(tuple(map(int, input().split())))

data.sort(key = lambda x: x[0])

for l, h in data:
    if h >= high_h:
        answer += (l - high_l) * high_h
        high_l, high_h = l, h
        stack = []
    else:
        stack.append((data[-1][0] - l, h))

stack = stack[::-1]
stack.append((data[-1][0] - high_l, high_h))
high_l, high_h = -1, 0

for l, h in stack:
    if h >= high_h:
        answer += (l - high_l) * high_h
        high_l, high_h = l, h
        
print(answer + high_h)