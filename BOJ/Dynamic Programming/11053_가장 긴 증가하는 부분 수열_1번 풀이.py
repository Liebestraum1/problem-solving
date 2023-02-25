n = int(input())
data = list(map(int, input().split()))
answer = [(1, data[0])]

for value in data[1:]:
    l = 0
    for c in answer:
        if c[1] < value and c[0] > l:
            l = c[0]
    if l == 0:
        answer.append((1, value))
    else:
        answer.append((l + 1, value))
        
print(max(answer, key = lambda x: x[0])[0])