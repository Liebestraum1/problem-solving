def solution(s): #회전시 deque 사용해도 됨
    def right(a):
        stack = [0]
        for p in a:
            stack.append(p)
            if stack[-1] == ']':
                if stack[-2] == '[':
                    stack = stack[:-2]
            elif stack[-1] == '}':
                if stack[-2] == '{':
                    stack = stack[:-2]
            elif stack[-1] == ')':
                if stack[-2] == '(':
                    stack = stack[:-2]
        return 1 if len(stack) == 1 else 0
    
    answer = 0
    for i in range(len(s)):
        if right(s[i:] + s[:i]):
            answer += 1
    return answer