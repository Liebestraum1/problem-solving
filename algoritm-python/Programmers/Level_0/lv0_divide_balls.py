#Programmers lv.0, 구슬을 나누는 경우의 수
def solution(balls, share):
    def factorial(n):
        k = 1
        for i in range(n, 1, -1):
            k *= i
        return k
    
    return factorial(balls) / (factorial(balls - share) * factorial(share))