def solution(progresses, speeds): #처음 풀이
    answer = []
    progresses = progresses[::-1]
    stack_speed = speeds[::-1]
    while True:
        stack = 0
        for i in range(len(progresses)):
            progresses[i] += stack_speed[i] #비효율적인 반복문
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            stack += 1
        if stack != 0:
            answer.append(stack)
        if not progresses:
            return answer

def solution(progresses, speeds):
    answer = []
    stack = 0
    time = 0
    while progresses:
        if progresses[0] + (time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            stack += 1
        else:
            if stack != 0:
                answer.append(stack)
            stack = 0
            time += 1
    answer.append(stack)
    return answer