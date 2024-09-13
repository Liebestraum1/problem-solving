def solution(s): 
    stack = []
    for i in s:
        stack.append(i)
        if stack[0] == ')':
            return False
        if len(stack) >= 2:
            if stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()
    return False if stack else True