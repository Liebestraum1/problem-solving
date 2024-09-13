def solution(rows, columns, queries):
    board = [[i + 1 for i in range(j, j + columns)] for j in range(0, rows * columns, columns)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -=1; y1 -=1; x2 -=1; y2 -=1;
        
        top = board[x1][y1:y2+1]
        right = list(list(zip(*board))[y2][x1+1:x2])
        bottom = board[x2][y1:y2+1][::-1]
        left = list(list(zip(*board))[y1][x1+1:x2])[::-1]

        width, height = len(top), len(right)
        rotate = top + right + bottom + left; rotate = [rotate.pop()] + rotate
        
        answer.append(min(rotate))
        
        top, right = rotate[:width], rotate[width:width + height]
        bottom, left = rotate[width+height:2*width+height][::-1], rotate[2*width+height:][::-1]
        
        board[x1][y1:y2+1] = top; board[x2][y1:y2+1] = bottom
        for i in range(height):
            board[x1+i+1][y2] = right[i]
            board[x1+i+1][y1] = left[i]
    return answer