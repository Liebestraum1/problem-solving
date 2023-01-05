from functools import cache
k = int(input())
def hannoi(n, start, end, via):
    if n == 1:
        print(start, end)
    else:
        hannoi(n-1, start, via, end)
        print(start, end)
        hannoi(n-1, via, end, start)

print(2 ** k - 1)
if k < 20:
    hannoi(k, 1, 3, 2)