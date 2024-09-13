for test in range(1, 11):
    answer = 0
    n = int(input())
    data = list(map(int, input().split()))
    for i in range(2, n-2):
        if data[i] > max(data[i-2:i] + data[i+1:i+3]):
            answer += data[i] - max(data[i-2:i] + data[i+1:i+3])
    print(f"#{test} {answer}")
