def solution(n):
    answer = 1
    n, r = n - 1, n - 2
    def factorial(n):
        k = 1
        for i in range(1, n+1):
            k *= i
        return k
    while r >= 0:
        if r != 0:
            answer += factorial(n) // (factorial(n-r)*factorial(r))
        if r == 0:
            answer += 1
        n -= 1; r -= 2
    return answer % 1234567