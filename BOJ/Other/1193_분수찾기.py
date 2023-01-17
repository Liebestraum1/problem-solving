x = int(input())
i = 0
while x > i * (i + 1) / 2:
    i += 1
x -= int(i * (i - 1) / 2)
print(f'{str(i-x+1)}/{str(x)}' if i % 2 != 0 else f'{str(x)}/{str(i-x+1)}')