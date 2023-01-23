n, m = map(int, input().split()) #n이 세로고 m이 가로
data = []
answer = []
b1 = (list('WBWBWBWB') + list('BWBWBWBW')) * 4
b2 = (list('BWBWBWBW') + list('WBWBWBWB')) * 4

for _ in range(n):
    data.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        board = []
        a1, a2 = 0, 0
        for k in range(8):
            board.append(data[i:i+8][k][j:j+8])
        board = [a for b in board for a in b]
        for l in range(len(board)):
            if board[l] != b1[l]:
                a1 += 1
            if board[l] != b2[l]:
                a2 += 1
        answer.append(a1)
        answer.append(a2)
            
print(min(answer))