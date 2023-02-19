N=int(input())
board = [0] * N
result = 0


def put(queen, board):
    for i in range(queen):
        if abs(board[queen] - board[i]) == abs(queen - i) or board[queen] == board[i]:
            return False
    return True

def Nqueens(queen, board=board):
    global result
    if queen == len(board):
        result += 1
        return
    for i in range(len(board)):
        board[queen] = i
        if put(queen, board):
            Nqueens(queen+1, board)

Nqueens(0)
print(result)