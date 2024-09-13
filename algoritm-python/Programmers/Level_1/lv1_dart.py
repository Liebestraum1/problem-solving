def solution(dartResult):
    stack = ""
    answer = []
    for v in dartResult:
        if v.isdigit():
            stack += v
        if not v.isdigit() and stack != "":
            answer.append(int(stack))
            stack = ""
        if v == 'D':
            answer[-1] **= 2
        if v == 'T':
            answer[-1] **= 3
        if v == '#':
            answer[-1] *= -1
        if v == '*':
            if len(answer) == 1:
                answer[-1] *= 2
            else:
                answer[-1] *= 2
                answer[-2] *= 2
    return sum(answer)