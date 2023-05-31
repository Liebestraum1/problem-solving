import sys
input = sys.stdin.readline
n, m = map(int, input().split()) #n = 행, m = 열, 최대 500 x 500
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

def brute_force():
    answer = 0
    for row in range(n):
        for col in range(m):
            if row + 1 < n and col + 1 < m: #1 정사각형 블록
                answer = max(answer, board[row][col] + board[row+1][col] + board[row][col+1] + board[row+1][col+1])
            if row + 3 < n: #2 바 형태의 블록 세로
                answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row+3][col])
            if col + 3 < m: #3 바 형태의 블록 가로
                answer = max(answer, sum(board[row][col:col+4]))
            if row + 2 < n: #4 세로 3칸
                if col - 1 >= 0:
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row+1][col-1]) #4-1 ㅓ
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row][col-1]) # 4-2 ┐
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row+2][col-1]) #4-3 ┘
                if col + 1 < m:
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row+1][col+1]) #4-4 ㅏ
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row][col+1]) #4-5 ┌
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+2][col] + board[row+2][col+1]) #4-6 └
                    answer = max(answer, board[row][col] + board[row+1][col] + board[row+1][col+1] + board[row+2][col+1])
                    answer = max(answer, board[row][col+1] + board[row+1][col+1] + board[row+1][col] + board[row+2][col])
            if col + 2 < m:#5 가로 3칸
                if row - 1 >= 0:
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row-1][col+1]) #5-1 ㅗ
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row-1][col]) #5-2 └─ 
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row-1][col+2]) #5-3 
                if row + 1 < n: # ㅜ
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row+1][col+1])
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row+1][col])
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row][col+2] + board[row+1][col+2])
                    answer = max(answer, board[row][col] + board[row][col+1] + board[row+1][col+1] + board[row+1][col+2])
                    answer = max(answer, board[row][col+1] + board[row][col+2] + board[row+1][col] + board[row+1][col+1])
        return answer

def dfs()