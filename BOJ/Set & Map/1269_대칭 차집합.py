data = input()
answer = set()

for i in range(1, len(data)+1):
    for j in range(len(data) - i + 1):
        answer.add(data[j:i+j])

print(len(answer))