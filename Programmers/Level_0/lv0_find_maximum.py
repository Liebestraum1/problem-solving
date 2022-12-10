#Programmers lv.0, 가장 큰 수 찾기
def solution(array):
    m = [0, 0]
    for i, v in enumerate(array):
        if v > m[0]:
            m = [v, i]
    return m