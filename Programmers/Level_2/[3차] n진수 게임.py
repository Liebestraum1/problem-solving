def solution(n, t, m, p):
    num = '0123456789ABCDEF'
    game = ''
    answer = ''
    def s(k, n):
        result = ''
        while k > 0:
            result += num[k%n]
            k //= n
        return result[::-1] if result else '0'
    for i in range(p + 1 + (m * t)):
        game += s(i, n)
    for i in range(p-1, p + (m * t) - 1, m):
        answer += game[i]
    return answer