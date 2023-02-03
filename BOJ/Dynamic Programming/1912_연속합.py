n = int(input())
data = list(map(int, input().split()))
acc, answer = 0, max(data)

for i in data:
    if acc < 0:
        acc = 0
    acc += i
    if acc > answer:
        answer = acc
print(answer)