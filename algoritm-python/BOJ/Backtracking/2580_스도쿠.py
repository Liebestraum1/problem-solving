import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(9)]
answer = []

def sudoku(arr, row, col):
    if row == 9:
        for r in arr:
            print(*r)
        exit()
    else:
        if arr[row][col] != 0:
            sudoku(arr, row + (col+1)//9, (col+1)%9)
        else:
            can = arr[row] + [arr[i][col] for i in range(0, 9)] + [i[j] for i in arr[row//3*3:row//3*3+3] for j in range(col//3*3, col//3*3+3)]
            for num in range(1, 10):
                if num not in can:
                    arr[row][col] = num
                    sudoku(arr, row + (col+1)//9, (col+1)%9)
                    arr[row][col] = 0
sudoku(arr, 0, 0)