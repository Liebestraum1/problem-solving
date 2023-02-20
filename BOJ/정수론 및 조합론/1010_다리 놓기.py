import sys
input = sys.stdin.readline

def f(a):
    answer = 1
    if a < 2:
        return answer
    for i in range(2, a+1):
        answer *= i
    return answer

t = int(input())
for _ in range(t):
    r, n = map(int, input().split())
    print(int(f(n) / (f(r) * f(n-r))))