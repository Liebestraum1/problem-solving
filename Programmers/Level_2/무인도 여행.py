import sys
sys.setrecursionlimit(10 ** 6)

def solution(maps):
    answer = []
    visited = set()
    def dfs(r, c):
        if r < 0 or r >= len(maps) or c < 0 or c >= len(maps[0]) or (r, c) in visited or maps[r][c] == 'X':
            return 0
        if (r, c) not in visited:
            visited.add((r, c))
            return int(maps[r][c]) + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)        
        
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] != 'X' and (row, col) not in visited:
                answer.append(dfs(row, col))
    
    return sorted(answer) if answer else [-1]