#Programmers lv.0, 주사위의 개수
def solution(box, n):
    answer = 1
    box = [i // n for i in box]
    for i in box:
        answer *= i
    return answer