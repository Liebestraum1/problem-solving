def solution(n):
    answer = [[0] * i for i in range(1,n+1)]
    col, row = -1, 0
    i = 1
    while i <= sum(range(n+1)):
        while col + 1 < n and answer[col+1][row] == 0:
            answer[col+1][row] = i
            col += 1; i += 1
        while row + 1 < len(answer[col]) and answer[col][row+1] == 0:
            answer[col][row+1] = i
            row += 1; i += 1
        while col-1 > 0 and row-1 > 0 and answer[col-1][row-1] == 0:
            answer[col-1][row-1] = i
            col -= 1; row -= 1; i += 1
    return [i for j in answer for i in j]

print(solution(1000))