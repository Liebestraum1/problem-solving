def solution(name, yearning, photo):
    score = {name[i] : yearning[i] for i in range(len(name))}
    answer = []
    for p in photo:
        s = 0
        for people in p:
            if people in score:
                s += score[people]
        answer.append(s)
    return answer