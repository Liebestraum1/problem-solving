def solution(s): #파싱 잘못함, 비효율적
    answer = []
    result = []
    s = s[1:-1].replace('},', '}')
    flag = 0
    stack_int = ''
    for i in s:
        if i == '{':
            flag = 1
            stack_string = set()
            continue
        if i == '}':
            flag = 0
            stack_string.add(int(stack_int))
            answer.append(stack_string)
            stack_int = ''
            continue
        if i == ',':
            stack_string.add(int(stack_int))
            stack_int = ''
            continue
        stack_int += i
    
    answer.sort(key = lambda x: len(x))
    for i in range(len(answer)-1, 0, -1):
        answer[i] = answer[i] - answer[i-1]
    return [list(i)[0] for i in answer]

def solution(s): #파싱 똑바로
    s = s.lstrip('{').rstrip('}').split('},{')
    t = []
    answer = []
    
    for element in s:
        t.append(list(map(int, element.split(',')))) 
        
    t.sort(key = len)
    
    for i in t:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

import re