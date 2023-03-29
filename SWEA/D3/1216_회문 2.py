for test in range(1, 11):
    t = int(input())
    board = []
    for row in range(100):
        board.append(input())
    board_p = list(zip(*board))
    answer = 0

    for i in range(100, 0, -1):
        for row in range(100):
            for j in range(100 - i + 1):
                if board[row][j:j+i] == board[row][j:j+i][::-1] or board_p[row][j:j+i] == board_p[row][j:j+i][::-1]:
                    answer = i
                    break
            if answer:
                break
        if answer:
                break
    print(f"#{test} {answer}")