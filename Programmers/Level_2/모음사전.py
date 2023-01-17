def solution(word):
    answer = []
    depth = -1
    def vowel(start, goal):
        nonlocal depth
        depth += 1
        if start == goal:
            answer.append(depth)
        if len(start) < 5:
            for i in 'AEIOU':
                vowel(start + i, goal)
    vowel('', word)
    return answer[-1]

print(solution("AEE"))