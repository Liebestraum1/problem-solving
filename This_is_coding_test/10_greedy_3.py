data = input()
answer = [0, 0]
answer[int(data[-1])] += 1
stack = data[0]

for i in data:
    if i != stack:
        answer[int(stack)] += 1
        stack = i
print(min(answer))