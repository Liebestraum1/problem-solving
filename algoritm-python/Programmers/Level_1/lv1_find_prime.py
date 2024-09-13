#Programmers lv.1, 소수 찾기
def solution(n):
    a = {i for i in range(2, n+1)}
    for j in range(2, int(n**0.5) + 1):
        a -= {k for k in range(2 * j, n+1, j)}    
    return len(a)