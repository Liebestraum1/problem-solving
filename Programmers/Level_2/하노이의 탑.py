def solution(n):
    answer = []
    def recursive(n, start, end, through):
        if n == 1:
            answer.append([start, end])
        else:
            recursive(n-1, start, through, end)
            answer.append([start, end])
            recursive(n-1, through, end, start)
    recursive(n, 1, 3, 2)
    return answer