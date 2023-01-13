def solution(dirs):
    visited = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    d = ['R', 'L', 'U', 'D']
    x, y = 0, 0
    
    for move in dirs:
        for i in range(len(d)):
            if move == d[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > 5 or ny > 5 or nx < -5 or ny < -5:
                    continue
                if {(nx, ny), (x, y)} not in visited:
                    visited.append({(nx, ny), (x, y)})
                x, y = nx, ny
    return len(visited)