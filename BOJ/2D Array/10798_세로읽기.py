data = []
for _ in range(5):
    data.append(list(input()))

for row in data:
    while len(row) < len(max(data, key = len)):
        row.append('')

for col in zip(*data):
    print(*col, sep='', end='')