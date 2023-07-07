t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    board = []
    answer = [[0 for j in range(n+1)] for i in range(n+1)]
    result = 0

    for i in range(n):
        board.append(list(map(int, input().split())))

    for row in range(n):
        for col in range(n):
            answer[row+1][col+1] = answer[row+1][col] + board[row][col]

    for row in range(n):
        for col in range(n):
            answer[row+1][col+1] = answer[row+1][col+1] + answer[row][col+1]

    for i in range(m, n+1):
        for j in range(m, n+1):
            result = max(result, answer[i][j] - answer[i - m][j] - answer[i][j-m] + answer[i-m][j-m])

    print(f"#{case + 1} {result}")