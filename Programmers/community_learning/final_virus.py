def solution(rows, columns, max_virus, queries):
    answer = [[0 for col in range(columns)] for row in range(rows)]
    queries = [[row - 1, col - 1] for row, col in queries][::-1]
    stack = []

    while len(queries) != 0:
        visited = []
        stack.append(queries.pop())
        while len(stack) != 0:
            coord = stack.pop()
            if coord in visited:
                continue
            visited.append(coord)
            row = coord[0]
            col = coord[1]
            if answer[row][col] < max_virus:
                answer[row][col] += 1
            else:
                if row-1 >= 0:
                    stack.append([row-1, col])
                if row+1 <= rows-1:
                    stack.append([row+1, col])
                if col-1 >= 0:
                    stack.append([row, col-1])
                if col+1 <= columns-1:
                    stack.append([row, col+1])
    return answer