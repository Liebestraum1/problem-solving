def solution(n):
    answer = ''
    digit = ['1', '2', '4']
    while n > 0:
        answer += digit[n%3 - 1]
        if n%3 == 0:
            n = n//3 - 1
        else:
            n //= 3
    return answer[::-1]