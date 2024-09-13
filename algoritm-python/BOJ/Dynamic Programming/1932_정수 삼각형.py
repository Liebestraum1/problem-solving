n = int(input())

row = [0]
for _ in range(n):
    next_row = list(map(int, input().split()))
    for i in range(len(next_row)):
        if i == 0:
            next_row[i] += row[i]
        elif i == len(next_row) - 1:
            next_row[i] += row[-1]
        else:
            next_row[i] += max(row[i-1], row[i])
    row = next_row
print(max(row))