from collections import deque

n = int(input())
board = [['O' for i in range(n)] for j in range(n)]
board[0][0] = 'S'


k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 'A'
    
time = 0
direction_list = ["UP", "RIGHT", "DOWN", "LEFT"]
direction = 1
collision = False

def move(coordinate, d):
    row, col = coordinate
    if d == "UP":
        return (row - 1, col)
    if d == "DOWN":
        return (row + 1, col)
    if d == "RIGHT":
        return (row, col + 1)
    if d == "LEFT":
        return (row, col - 1)

def rotate(d, nd):
    if nd == 'L':
        d -= 1
    if nd == 'D':
        d += 1
    
    if d < 0:
        return 3
    elif d > 3:
        return 0
    else:
        return d

snake = deque([(0, 0)]) #시작부분이 꼬리, 끝부분이 머리

l = int(input())

for a in range(l+1):
    if a == l:
        turn_time = 100
    else:
        turn_time, next_direction = input().split()
        turn_time = int(turn_time)
    while time < turn_time:
        head = snake[-1]
        time += 1
        next_row, next_col = move(head, direction_list[direction])
        
        if next_row >= n or next_row < 0 or next_col >= n or next_col < 0 or board[next_row][next_col] == 'S':
            collision = True
            break
        elif board[next_row][next_col] == 'A':
            snake.append((next_row, next_col))
        else:
            snake.append((next_row, next_col))
            tail_row, tail_col = snake.popleft()
            board[tail_row][tail_col] = 'O'
        board[next_row][next_col] = 'S'
    
    if collision == True:
        print(time)
        break
    else:
        direction = rotate(direction, next_direction)