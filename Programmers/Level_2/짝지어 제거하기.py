def solution(s):
    s = list(s)
    answer = ['A']
    for i in s:
        if i == answer[-1]:
            answer.pop()
        else:
            answer += i
    return 1 if not answer[1:] else 0