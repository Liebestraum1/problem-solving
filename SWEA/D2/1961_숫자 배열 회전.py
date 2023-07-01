t = int(input())

for case in range(t):
    n = int(input())
    data = []
    answer = [[] for _ in range(n)]
    for i in range(n):
        data.append(list(map(int, input().split())))

    for i in range(3):
        data = list(map(lambda x: x[::-1], zip(*data)))
        for row in range(n):
            answer[row].append("".join(list(map(str, data[row]))))
    
    print(f"#{case + 1}")
    for i in answer:
        print(*i)