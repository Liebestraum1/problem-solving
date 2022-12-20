#Programmers lv.1, 나누어 떨어지는 배열
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]