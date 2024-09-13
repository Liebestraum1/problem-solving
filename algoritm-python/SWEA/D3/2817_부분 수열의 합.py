from itertools import combinations

t = int(input())

for test in range(1, t+1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    answer = 0
    for r in range(1, n+1):
        for c in combinations(data, r):
            if sum(c) == k:
                answer += 1
    print(answer)