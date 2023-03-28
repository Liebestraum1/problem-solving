t = int(input())

def nqueen(board, row):
    global answer
    if row == len(board):
        answer += 1
        return
    for col in range(len(board)):
        can = True
        for previous in range(row):
            if board[previous] == col or abs(row - previous) == abs(col - board[previous]):
                can = False
                break
        if can:
            board[row] = col
            nqueen(board, row+1)


for test in range(1, t+1):
    answer = 0
    n = int(input())
    t = [0 for _ in range(n)]
    nqueen(t, 0)
    print(f"#{test} {answer}")