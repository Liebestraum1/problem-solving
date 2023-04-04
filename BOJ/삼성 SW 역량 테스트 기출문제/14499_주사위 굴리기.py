n, m, x, y, k = map(int, input().split())

board = []
dice = [0, 0, 0, 0, 0, 0]
for _ in range(n):
    board.append(list(map(int, input().split())))

moving = list(map(int, input().split()))
#0번째 인덱스: 상단 위쪽    0
#1번째 인덱스: 상단 좌촉  1 2 3
#2번째 인덱스: 상단 정면    4
#3번째 인덱스: 상단 우측    5
#4번째 인덱스: 상단 아래쪽
#5번째 인덱스: 상단 반대편

def cast(d, direction, dx, dy):
    if direction == 1: #우측으로 굴릴 경우
        return [d[0], d[5], d[1], d[2], d[4], d[3]], x, y+1
    if direction == 2: #좌측으로 굴릴 경우
        return [d[0], d[2], d[3], d[5], d[4], d[1]], x, y-1
    if direction == 3: #위로
        return [d[2], d[1], d[4], d[3], d[5], d[0]], x-1, y
    if direction == 4: #아래로
        return [d[5], d[1], d[0], d[3], d[2], d[4]], x+1, y

for move in moving:
    next_dice, nx, ny = cast(dice, move, x, y)
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    else:
        dice, x, y = next_dice, nx, ny
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[2])