for test in range(1, 11):
    answer = 0
    data = []
    t = int(input())
    t_diagonal, d_diagonal = 0, 0
    for _ in range(100):
        data.append(list(map(int, input().split())))
    
    for i in range(100):
        s = max(sum(list(zip(*data))[i]), sum(data[i]))
        t_diagonal += data[i][i]
        d_diagonal += data[99-i][i]
        if answer < s:
            answer = s
    
    answer = max(answer, t_diagonal, d_diagonal)
    print(f"#{test} {answer}")