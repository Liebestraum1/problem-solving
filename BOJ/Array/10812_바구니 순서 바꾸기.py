n, m = map(int, input().split())
data = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(lambda x: int(x) - 1, input().split())
    data[i:j+1] = data[k:j+1] + data[i:k]

print(*data)