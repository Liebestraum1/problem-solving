def solution(priorities, location): #복잡하게 풀었음
    answer = 0
    while len(priorities) > 1:
        stack = priorities.pop(0)
        if max(priorities) > stack:
            priorities.append(stack)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -=1
        else:
            answer += 1
            if location == 0:
                return answer
            stack = 0
            location -= 1
    return answer + 1

