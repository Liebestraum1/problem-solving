n = int(input())
data = []
answer = []
for i in range(n):
    data.append(int(input()))

for i in data:
    if not answer:
        answer.append(i)
    else:
        for j in range(len(answer)):
            if i < answer[j]:
                answer.insert(j, i)
                break
            elif j == len(answer) - 1:
                answer.append(i)

print(*answer, sep='\n')