#Programmers lv.1, 나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(2, int(n**0.5)+1):
        if (n-1) % i == 0:
            return i
    return n-1