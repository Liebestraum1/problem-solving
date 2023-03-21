from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = []

    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'S':
                start = (row, col, 0)
            if maps[row][col] == 'L':
                lever = (row, col, 0)
            if maps[row][col] == 'E':
                end = (row, col, 0)
    order = [[start, lever], [lever, end]]
    
    for s, e in order:
        visited = set(s)
        queue = deque([s])
        answer = -1
        while queue:
            x, y, t = queue.popleft()
            if (x, y) == (e[0], e[1]):
                answer = t
                break
            for i in range(4):
                mx, my = x + dx[i], y + dy[i]
                if mx < 0 or mx >= len(maps) or my < 0 or my >= len(maps[0]) or (mx, my) in visited or maps[mx][my] == 'X':
                    continue
                queue.append((mx, my, t+1))
                visited.add((mx, my))
        if answer == -1:
            return -1
        result.append(answer)
    return sum(result)