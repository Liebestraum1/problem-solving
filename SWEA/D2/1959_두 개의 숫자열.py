t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = 0

    if n > m:
        for i in range(n - m + 1):
            temp = 0
            for j in range(m):
                temp += a[j+i] * b[j]
            answer = max(answer, temp)
    else:
        for i in range(m - n + 1):
            temp = 0
            for j in range(n):
                temp += a[j] * b[j+i]
            answer = max(answer, temp)
    print(f"#{case + 1} {answer}")