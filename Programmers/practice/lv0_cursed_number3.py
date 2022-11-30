#Programmers lv.0, 저주의 숫자 3

def solution(n):
    answer = 0
    def divide(a):
        if a % 10 == 3:
            return 3
        if a < 10:
            return a
        return divide(a//10)
    
    while n:
        n -= 1
        answer += 1
        while answer % 3 == 0 or divide(answer) == 3:
            answer += 1
    return answer