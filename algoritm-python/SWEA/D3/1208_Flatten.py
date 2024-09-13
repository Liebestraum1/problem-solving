for test in range(1, 11):
    dump = int(input())
    start, end = 0, 99
    data = sorted(list(map(int, input().split())))
    while dump and data[end] - data[start] > 1:
        dump -= 1
        data[end] -= 1
        data[start] += 1

        if data[start] > data[start + 1]:
            start += 1
        else:
            start = 0
        if data[end] < data[end - 1]:
            end -= 1
        else:
            end = 99
    print(f"#{test} {data[end] - data[start]}")