import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))