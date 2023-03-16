import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

bw = list('BW' * (m // 2) if m % 2 == 0 else 'BW' * (m // 2) + 'B')
wb = list('WB' * (m // 2) if m % 2 == 0 else 'WB' * (m // 2) + 'W')

array = []
sol_bw = []
sol_wb = []
answer_bw = [[0] * (m+1)]
answer_wb = [[0] * (m+1)]
result = k * k

for i in range(n):
    if i % 2 == 0:
        sol_bw.append(bw)
        sol_wb.append(wb)
    else:
        sol_bw.append(wb)
        sol_wb.append(bw)

for _ in range(n):
    array.append(list(input().rstrip()))

for row in range(n):
    rbw = [0, 0 if array[row][0] == sol_bw[row][0] else 1]
    rwb = [0, 0 if array[row][0] == sol_wb[row][0] else 1]
    for col in range(1, m):
        rbw.append(rbw[-1] + (0 if array[row][col] == sol_bw[row][col] else 1))
        rwb.append(rwb[-1] + (0 if array[row][col] == sol_wb[row][col] else 1))
    answer_bw.append(rbw)
    answer_wb.append(rwb)

for row in range(1, n+1):
    for col in range(1, m+1):
        answer_bw[row][col] = answer_bw[row-1][col] + answer_bw[row][col]
        answer_wb[row][col] = answer_wb[row-1][col] + answer_wb[row][col]

for row in range(k, n+1):
    for col in range(k, m+1):
        r1 = answer_bw[row][col] - answer_bw[row-k][col] - answer_bw[row][col-k] + answer_bw[row-k][col-k]
        r2 = answer_wb[row][col] - answer_wb[row-k][col] - answer_wb[row][col-k] + answer_wb[row-k][col-k]
        result = min(r1, r2, result)

print(result)