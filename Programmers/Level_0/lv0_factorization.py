#Programmers lv.0, 소인수분해
def solution(n):
    i = 2
    answer = []
    while i <= n:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n = n // i
            i == 2
        else:
            i += 1
    return answer