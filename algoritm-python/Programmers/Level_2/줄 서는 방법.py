def factorial(num):
    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f

def solution(n, k):
    stack = [i for i in range(1, n+1)]
    answer, idx = [], 1
    while stack:
        for i in range(len(stack)):
            if (i+1) * factorial(n-idx) >= k:
                answer.append(stack.pop(i))
                if i > 0:
                    k -= i * factorial(n-idx)
                idx += 1
                break
    return answer