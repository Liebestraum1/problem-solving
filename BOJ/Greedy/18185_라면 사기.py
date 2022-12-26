import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a += [0, 0]

answer = 0

for i in range(len(a) - 2):
    if a[i] != 0:
        if a[i+1] > a[i+2]:
            if a[i+1] - a[i+2] >= a[i]:
                answer += a[i] * 5
                a[i+1] -= a[i]
                a[i] = 0
                continue
            else:
                answer += (a[i+1] - a[i+2]) * 5
                a[i] -= a[i+1] - a[i+2]
                a[i+1] -= a[i+1] - a[i+2]
        if a[i+1] > 0 and a[i+2] > 0:
            temp = min(a[i], a[i+1], a[i+2])
            a[i] -= temp
            a[i+1] -= temp
            a[i+2] -= temp
            answer += 7 * temp
        if a[i] > 0 and a[i+1] > 0:
            temp = min(a[i], a[i+1])
            a[i] -= temp
            a[i+1] -= temp
            answer += 5 * temp
        if a[i] > 0:
            answer += a[i] * 3
            a[i] = 0
print(answer)