def solution(numbers):
    stack = []
    answer = [0] * len(numbers)
    for i, n in enumerate(numbers):
        while stack and n > stack[-1][1]:
            answer[stack.pop()[0]] = n
        stack.append((i, n))
    answer = [-1 if v == 0 else v for v in answer]
    return answer