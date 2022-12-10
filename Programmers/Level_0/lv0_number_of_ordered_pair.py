#Programmers lv.0, 순서쌍의 개수
def solution(n):
    divisor = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisor.add((i, n//i))
    return len(divisor)