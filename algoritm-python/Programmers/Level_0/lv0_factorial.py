#Programmers lv.0, 팩토리얼
def solution(n):
    fac = 1
    i = 0
    while fac <= n:
        i += 1
        fac = fac * i
    return i-1