def solution(ingredient):
    stack = [0, 0, 0, 0]
    hamburger = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            stack[-4:] = []
            hamburger += 1
    return hamburger