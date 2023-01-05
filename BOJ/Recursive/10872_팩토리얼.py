import sys
input = sys.stdin.readline
n = int(input())
answer = 1

for i in range(n, 0, -1): #반복문 이용
    answer *= i

def factorial(n): #재귀 이용
    if n < 2:
        return 1
    return n * factorial(n-1)

print(answer)