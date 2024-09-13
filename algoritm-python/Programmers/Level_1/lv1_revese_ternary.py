#Programmers lv.1, 3진법 뒤집기
def solution(n):
    answer = ''
    while n:
        answer += str(n%3)
        n = n//3       
    return int(answer, 3)