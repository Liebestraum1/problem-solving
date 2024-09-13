t = int(input())

for _ in range(t):
    num = int(input())
    data = list(map(int, input().split()))
    table = {}

    for i in data:
        table[i] = table.get(i, 0) + 1
    
    print(f"#{num} {max(table.items(), key = lambda x: x[1])[0]}")