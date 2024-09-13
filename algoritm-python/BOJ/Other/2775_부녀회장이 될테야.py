import sys
sys.setrecursionlimit(10 ** 6)
t = int(input())

def f(a, b): #a는 층수, b는 호수
    if a == 0 or b == 1:
        return b
    if (a, b) in dic:
        return dic[(a, b)]
    else:
        dic[(a, b)] = f(a-1, b) + f(a, b-1)
        return dic[(a, b)]

for _ in range(t):
    k = int(input())
    n = int(input())
    dic = {}
    print(f(k, n))