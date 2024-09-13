def solution(n):
    answer = 0
    board = [0] * n
    def check(row, board):
        for i in range(row):
            if board[row] == board[i] or abs(board[row] - board[i]) == row - i:
                return False
        return True

    def Nqueen(queen):
        nonlocal answer
        if queen == n:
            answer += 1
            return
        for i in range(n):
            board[queen] = i
            if check(queen, board):
                Nqueen(queen+1)
    Nqueen(0)
    return answer