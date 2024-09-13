n = int(input())
x, y = 0, 0
coord = []
for _ in range(6):
    direction, moving = map(int, input().split())
    if direction == 1: x += moving
    elif direction == 2: x -= moving
    elif direction == 3: y -= moving
    else: y += moving
    coord.append((x, y))

sx = min(coord, key = lambda x: x[0])[0]
sy = min(coord, key = lambda x: x[1])[1]
bx = max(coord, key = lambda x: x[0])[0]
by = max(coord, key = lambda x: x[1])[1]

big = (bx - sx) * (by - sy)
for i in (sx, bx):
    for j in (sy, by):
        if (i, j) not in coord:
            r = (i, j)
small = abs((sorted(coord, key = lambda x: x[0])[2][0] - r[0])) * abs((sorted(coord, key = lambda x: x[1])[2][1] - r[1]))

print((big - small) * n)