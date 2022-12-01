#Programmers lv.0, 최댓값 만들기 (1)
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]