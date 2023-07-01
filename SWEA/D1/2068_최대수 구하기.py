t = int(input())

for case in range(t):
    data = list(map(int, input().split()))
    answer = 0
    for i in range(len(data)):
        if data[i] % 2 == 1:
            answer += data[i]
    print(f"#{case + 1} {answer}")