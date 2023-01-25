n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

answer = [1 for _ in range(n)]

for i in range(len(data)):
    for j in data[:i] + data[i+1:]:
        if data[i][0] < j[0] and data[i][1] < j[1]:
            answer[i] += 1

print(*answer)