#구현 1. 상하좌우 (내 풀이)
n = int(input())
data = input().split()
answer = [1, 1]

for i in data:
    if i == 'U':
        if answer[0] != 1:
            answer[0] -= 1
    if i == 'D':
        if answer[0] != n:
            answer[0] += 1
    if i == 'L':
        if answer[1] != 1:
            answer[1] -= 1
    if i == 'R':
        if answer[1] != n:
            answer[1] += 1
print(answer)