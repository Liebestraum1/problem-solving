#Prgorammers lv.1, 문자열 나누기
def solution(s):
    stack = [0, 0]
    cut = 1
    answer = 0
    
    for v in s:
        if cut:
            cut = 0
            letter = v

        if letter == v:
            stack[0] += 1
        else:
            stack[1] += 1

        if stack[0] == stack[1]:
            answer += 1
            stack = [0, 0]
            cut = 1
    
    return answer if stack == [0,0] else answer + 1