#Programmers lv.1, 푸드 파이트 대회
def solution(food):
    answer = ''
    for order, cnt in enumerate(food[1:], 1):
        answer += str(order) * (cnt//2)
    return answer + '0' + answer[::-1]