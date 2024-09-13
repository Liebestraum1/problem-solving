def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -=1
            answer += 1
    return answer

def solution(n): #이진법 사용
    return bin(n).count('1')