n = int(input())
paper = [[0 for x in range(100)] for y in range(100)]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for row in paper:
    answer += row.count(1)
print(answer)