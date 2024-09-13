#Programmers lv.0, n의 배수 고르기
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]