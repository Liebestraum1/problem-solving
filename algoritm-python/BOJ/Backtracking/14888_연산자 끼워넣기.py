import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split())) #(+, -, *, /)

answer = []

def bt(r, op, k): #각 재귀마다 수를 넘겨줌(r)
    if k == len(data):
        answer.append(r)
        return
    for i in range(4):
        if op[i] != 0:
            op[i] -= 1
            if i == 0:
                bt(r + data[k], op, k+1)
            elif i == 1:
                bt(r - data[k], op, k+1)
            elif i == 2:
                bt(r * data[k], op, k+1)
            elif i == 3:
                if r <= 0:
                    bt((-r // data[k]) * (-1), op, k+1)
                else:
                    bt(r // data[k], op, k+1)
            op[i] += 1
bt(data[0], operator, 1)
answer.sort()
print(answer[-1], answer[0], sep='\n')