def solution(cards):
    answer = []
    for i in range(len(cards)):
        cnt = 0
        while cards[i]:
            temp = i
            cnt += 1
            i = cards[i] - 1
            cards[temp] = False
        if cnt != 0:
            answer.append(cnt)
    answer.sort()
    return 0 if len(answer) == 1 else answer[-1] * answer[-2]