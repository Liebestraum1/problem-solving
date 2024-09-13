n, m = map(int, input().split())
r, c, d = map(int, input().split())

dr = [-1, 0, 1, 0] #r이 빠지면 북쪽, r이 더해지면 남쪽
dc = [0, 1, 0, -1] #동, 서
board = []
can = True
answer = 0


def turn(n, x):
    return (n + 3 * x) % 4

for _ in range(n):
    board.append(list(map(int, input().split())))

while can:
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1

    for i in range(1, 5): # 1은 90도, 2는 180도, 3은 270도, 4는 원점
        nr, nc = r + dr[turn(d, i)], c + dc[turn(d, i)]
        if 0 <= nr and nr < n and 0 <= nc and nc < m and board[nr][nc] == 0:
            r, c = nr, nc
            d = turn(d, i)
            break
        elif i == 4 and ((r - dr[d] < 0 or r - dr[d] >= n or c - dc[d] < 0 or c - dc[d] >= m) or board[r - dr[d]][c - dc[d]] == 1):
            can = False
            break
        elif i == 4 and 0 <= r - dr[d] < n and 0 <= c - dc[d] < m:
            r, c = r - dr[d], c - dc[d]
            break

print(answer)
# print(*board, sep='\n')
# print(f"현재 세로: {r}, 현재 가로: {c}, 현재 방향: {d}")
# print(f"만약 이동하면 옮겨질 세로 좌표: {r + dr[turn(d, i)]}, 가로 좌표 {c + dc[turn(d, i)]}")
# print(f"해당 좌표의 값: {board[r + dr[turn(d, i)]][c + dc[turn(d, i)]]}")
# print(r - dr[d], c - dc[d])