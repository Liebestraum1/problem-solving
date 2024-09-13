def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        stack = ''
        for k in s:
            if k in skill:
                stack += k
        if stack == skill[:len(stack)]:
            answer += 1
    return answer