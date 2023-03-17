import sys
input = sys.stdin.readline

string = input().rstrip()
q = int(input())

answer = {}

for alphabet in "abcdefghijklmnopqrstuvwxyz":
    if alphabet not in answer:
        answer[alphabet] = [0] * range(len(string)+1)
        for i in range(len(string)):
            if alphabet == string[i]:
                answer[alphabet][i+1] = answer[alphabet][i]
            answer[alphabet].append(cnt)

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    if l == 0:
        print(answer[a][r])
    else:
        print(answer[a][r] - answer[a][l-1])