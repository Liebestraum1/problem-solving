def solution1(maps):
    m, n = (len(maps), len(maps[0])) #n = 가로(x), m = 세로(y)
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    def moving(x, y, depth, visited = [(1, 1)]):
        if (x, y) == (n, m):
            answer.append(depth)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx > n or nx < 1 or ny > m or ny < 1 or maps[ny-1][nx-1] == 0:
                continue
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                moving(nx, ny, depth+1, visited)
                visited.pop()
    
    moving(1, 1, 1)
    return min(answer) if answer != [] else -1

#상기한 코드는 DFS를 이용한 코드로, 효율성 테스트에서 문제 발생함

from collections import deque
def solution(maps):
    m, n = (len(maps), len(maps[0]))
    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    visited = {(1, 1)}; queue = deque([(1, 1)])
    distance = {(1, 1) : 1}

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n, m):
            print(visited)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx > n or nx < 1 or ny > m or ny < 1 or maps[ny-1][nx-1] == 0:
                continue
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                if (nx, ny) == (n, m):
                    return distance[(nx, ny)]
    return -1