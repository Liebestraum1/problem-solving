import sys
sys.setrecursionlimit(10 ** 6)

def solution(grid):
    answer = []
    visited = set()
    d = ['row_up', 'row_down', 'col_left', 'col_right']
    def refraction(row, col, direction, start, length):
        if length > 0 and (row, col, direction) == start:
            answer.append(length)
            return
        if (row, col, direction) in visited:
            return
        visited.add((row, col, direction))
        rotate = grid[row][col]
        if rotate == 'L':
            if direction == 'col_left':
                next_row, next_col, next_direction = row - 1, col, 'row_down'
            elif direction == 'col_right':
                next_row, next_col, next_direction = row + 1, col, 'row_up'
            elif direction == 'row_up':
                next_row, next_col, next_direction = row, col + 1, 'col_left'
            elif direction == 'row_down':
                next_row, next_col, next_direction = row, col - 1, 'col_right'
        elif rotate == 'R':
            if direction == 'col_left':
                next_row, next_col, next_direction = row + 1, col, 'row_up'
            elif direction == 'col_right':
                next_row, next_col, next_direction = row - 1, col, 'row_down'
            elif direction == 'row_up':
                next_row, next_col, next_direction = row, col - 1, 'col_right'
            elif direction == 'row_down':
                next_row, next_col, next_direction = row, col + 1, 'col_left'
        else: #rotate == 'S'
            if direction == 'col_left':
                next_row, next_col, next_direction = row, col + 1, direction
            elif direction == 'col_right':
                next_row, next_col, next_direction = row, col - 1, direction
            elif direction == 'row_up':
                next_row, next_col, next_direction = row + 1, col, direction
            elif direction == 'row_down':
                next_row, next_col, next_direction = row - 1, col, direction
        if next_row < 0:
            return refraction(len(grid)-1, next_col, next_direction, start, length + 1)
        elif next_row >= len(grid):
            return refraction(0, next_col, next_direction, start, length + 1)
        elif next_col < 0:
            return refraction(next_row, len(grid[0])-1, next_direction, start, length + 1)
        elif next_col >= len(grid[0]):
            return refraction(next_row, 0, next_direction, start, length + 1)
        else:
            return refraction(next_row, next_col, next_direction, start, length + 1)
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for m in d:
                refraction(row, col, m, (row, col, m), 0)
    
    return sorted(answer)