#Programmers lv.0, 최댓값 만들기(2)
def solution(numbers):
    numbers.sort()
    positive = numbers[-1] * numbers[-2]
    negative = numbers[0] * numbers[1]
    return positive if positive > negative else negative