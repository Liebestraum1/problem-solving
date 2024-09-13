t = int(input())

for test in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in data:
        if i <= sum(data) / len(data):
            answer += 1
    print(f"#{test} {answer}")