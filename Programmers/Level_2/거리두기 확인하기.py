def solution(places):
    answer = []
    d1 = [(1, 0, 2, 0), (-1, 0, -2, 0), (0, 1, 0, 2), (0, -1, 0, -2)]
    d2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    #move = row, col 순서
    for place in places:
        flag = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    for rm, cm, rmd, cmd in d1:
                        if row + rm < 0 or row + rm > 4 or col + cm < 0 or col + cm > 4:
                            continue
                        if place[row + rm][col + cm] == 'P':
                            flag = 0
                            break
                        if place[row + rm][col + cm] == 'O':
                            if row + rmd < 0 or row + rmd > 4 or col + cmd < 0 or col + cmd > 4:
                                continue
                            if place[row + rmd][col + cmd] == 'P':
                                flag = 0
                                break
                    if not flag:
                        break
                    for rm, cm in d2:
                        if row + rm < 0 or row + rm > 4 or col + cm < 0 or col + cm > 4:
                            continue
                        if place[row + rm][col + cm] == "P":
                            if place[row + rm][col] != "X" or place[row][col + cm] != "X":
                                flag = 0
                                break
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer