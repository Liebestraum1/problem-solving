#Programmers lv.1, 이상한 문자 만들기
def solution(s):
    idx = 0
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
            idx = 0
        else:
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            idx += 1
    return answer