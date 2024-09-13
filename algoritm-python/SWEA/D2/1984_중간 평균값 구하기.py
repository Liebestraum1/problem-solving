t = int(input())
for test in range(1, t+1):
    data = sorted(list(map(int, input().split())))
    answer = round(sum(data[1:9]) / 8)
    print(f"#{test} {answer}")