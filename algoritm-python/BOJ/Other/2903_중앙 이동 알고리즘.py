n = int(input())
data = [0 for _ in range(16)]
data[0] = 2

for i in range(1, 16):
    data[i] = data[i-1] * 2 - 1

for i in range(16):
    data[i] = data[i] ** 2

print(data[n])