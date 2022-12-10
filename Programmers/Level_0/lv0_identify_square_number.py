#Programmers lv.0, 제곱수 판별하기
def solution(n):
    if n ** 0.5 == int(n ** 0.5):
        return 1
    return 2