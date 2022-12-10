#Programmers lv.0, 유한소수 판별하기

def solution(a, b):
    def gcd(i, j):
        if i % j == 0:
            return j
        return gcd(j, i%j)
    
    b = b // gcd(a, b)
    
    while b % 2 == 0:
        b = b /2
    while b % 5 == 0:
        b = b /5
    
    if b == 1:
        return 1
    else:
        return 2
    
    return answer