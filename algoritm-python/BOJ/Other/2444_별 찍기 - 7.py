n = int(input())

for i in range(1, 2 * n):
    print(" " * abs(n-i) + "*" * (2 * (n - abs(n - i)) - 1))