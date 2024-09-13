#Programmers lv.1, 콜라 문제
def solution(a, b, n): #a는 주는병, b는 받는 콜라병, n은 보유중인 공병
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = b * (n // a) + (n % a)
    return answer