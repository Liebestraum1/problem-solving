#Programmers lv.0, 컨트롤 제트
def solution(s):
    answer = 0
    for i in s.replace(' Z', 'Z').split():
        if "Z" not in i:
            answer += int(i)
    return answer