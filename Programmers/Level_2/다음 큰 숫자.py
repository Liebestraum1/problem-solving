def solution(n):
    one = format(n, 'b').count('1')
    answer = n
    while True:
        answer += 1
        if format(answer, 'b').count('1') == one:
            return answer