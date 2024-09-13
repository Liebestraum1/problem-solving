t = int(input())
for test in range(1, t+1):
    n = int(input())
    answer = 0
    s = n // 2
    for row in range(n):
        data = list(map(int, input()))
        if s == 0:
            answer += sum(data)
        else:
            answer += sum(data[abs(s):-abs(s)])
        s -= 1
    print(f"#{test} {answer}")