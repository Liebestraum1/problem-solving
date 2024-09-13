t = int(input())
for test in range(t):
    n = int(input())
    data = {}
    answer = 1
    for case in range(n):
        clothes, type = input().split()
        data[type] = data.get(type, 1) + 1
    for count in data.values():
        answer *= count
    print(answer - 1)