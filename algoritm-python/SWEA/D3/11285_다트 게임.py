t = int(input())
board = [0 for _ in range(80001)]
for s in range(0, 200, 20):
    k = s // 20
    for j in range(s * s + 1, (s + 20) * (s + 20) + 1):
        board[j] = 10 - k
board[0] = 10

answer = []

for test in range(1, t+1):
    dart = int(input())
    score = 0
    for d in range(dart):
        x, y = map(int, input().split())
        score += board[x * x + y * y]
    answer.append(f'#{test} {score}')

for a in answer:
    print(a)