#Programmers lv.0, 배열의 유사도
def solution(s1, s2):
    return len(set(s1)&set(s2))