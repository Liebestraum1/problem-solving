import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = list(range(1,n + 1))

def permutations(arr, k, answer = []):
    if k == 0:
        return print(*answer)
    else:
        for i in range(len(arr)):
            permutations(arr[:i] + arr[i+1:], k-1, answer + [arr[i]])

permutations(a, m)