from collections import deque

n, m = map(int, input().split())
board = []
answer = []
direction = ['UP', 'DOWN', 'LEFT', 'RIGHT']
visited = set()


def move(dr, row, col):
    if dr == 'UP':
        while board[row][col] != 'O' and board[row - 1][col] != '#':
            row -= 1
        return row
    if dr == 'DOWN':
        while board[row][col] != 'O' and board[row + 1][col] != '#':
            row += 1
        return row
    if dr == 'LEFT':
        while board[row][col] != 'O' and board[row][col - 1] != '#':
            col -= 1
        return col
    if dr == 'RIGHT':
        while board[row][col] != 'O' and board[row][col + 1] != '#':
            col += 1
        return col


for i in range(n):
    row = input()
    if 'R' in row:
        red_row, red_col = i, row.index('R')
    if 'B' in row:
        blue_row, blue_col = i, row.index('B')
    board.append(row)

queue = deque([(red_row, red_col, blue_row, blue_col, 0)])
while queue:
    rr, rc, br, bc, cnt = queue.popleft()
    visited.add((rr, rc, br, bc))
    if board[br][bc] == 'O':
        continue
    if board[rr][rc] == 'O':
        answer.append(cnt)
        continue
    for d in direction:
        if d == 'UP':
            nrc, nbc, nrr, nbr = rc, bc, move(d, rr, rc), move(d, br, bc)
            if nrc == nbc and nrr == nbr and board[nbr][nbc] != 'O':
                if rr < br:
                    nbr += 1
                elif rr > br:
                    nrr += 1
        if d == 'DOWN':
            nrc, nbc, nrr, nbr = rc, bc, move(d, rr, rc), move(d, br, bc)
            if rc == bc and nrr == nbr and board[nbr][nbc] != 'O':
                if rr < br:
                    nrr -= 1
                elif rr > br:
                    nbr -= 1
        if d == 'LEFT':
            nrr, nbr, nrc, nbc = rr, br, move(d, rr, rc), move(d, br, bc)
            if rr == br and nrc == nbc and board[nbr][nbc] != 'O':
                if rc < bc:
                    nbc += 1
                elif rc > bc:
                    nrc += 1
        if d == 'RIGHT':
            nrr, nbr, nrc, nbc = rr, br, move(d, rr, rc), move(d, br, bc)
            if rr == br and nrc == nbc and board[nbr][nbc] != 'O':
                if rc < bc:
                    nrc -= 1
                elif rc > bc:
                    nbc -= 1
        if (nrr, nrc, nbr, nbc) not in visited:
            queue.append((nrr, nrc, nbr, nbc, cnt + 1))

print(min(answer) if answer else -1)