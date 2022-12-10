#Programmers lv.0, 숫자 찾기
def solution(num, k):
    for i, v in enumerate(str(num), 1):
        if str(k) == v:
            return i
    return -1