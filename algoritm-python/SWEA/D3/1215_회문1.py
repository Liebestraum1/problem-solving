for test in range(1, 11):
    n = int(input())
    answer = 0
    data = []
    for _ in range(8):
        data.append(input())
    
    data_pivot = list(zip(*data))

    for i in range(8):
        for j in range(8 - n + 1):
            if data[i][j:j + n] == data[i][j:j + n][::-1]:
                answer += 1
            if data_pivot[i][j:j + n] == data_pivot[i][j:j + n][::-1]:
                answer += 1
    print(f"#{test} {answer}")