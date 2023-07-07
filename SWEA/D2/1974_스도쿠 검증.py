t = int(input())

for case in range(t):
    board = []
    answer = 1
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    
    pivot = list(zip(*board))
    for i in range(9):
        if len(set(pivot[i])) != 9 or len(set(board[i])) != 9:
            answer = 0
            break

    if answer != 0:
        for row_sector in range(0, 9, 3):
             for col_sector in range(0, 9, 3):
                    data = set()
                    for row in range(3):
                        for col in range(3):
                            data.add(board[row_sector + row][col_sector + col])
                    if len(data) != 9:
                        answer = 0
                        break

    print(f"#{case + 1} {answer}")