from collections import deque
def solution(people, limit): #deque 사용
    answer = 0
    people = deque(sorted(people))
    
    while people:
        light = people.popleft()
        while people and limit - light < people[-1]:
            people.pop()
            answer += 1
        if people:
            people.pop()
        answer += 1
    return answer

def solution(people, limit): #deque 사용 안함
    answer = 0
    people.sort()
    
    light = 0
    heavy = len(people) - 1
    
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
    return answer