#Programmers lv.1, 실패율 
def solution(N, stages):
    answer = {i : 0 for i in range(1, N+1)}
    stages.sort()
    stages.append(N+1)    
    acc = 0
    stage = stages[0]

    for i, v in enumerate(stages, 1):
        if v != stage:
            answer[stage] = (i - 1 - acc) / (len(stages) - acc - 1)
            stage = v
            acc = i-1
    return [i[0] for i in sorted(answer.items(), key = lambda x: x[1], reverse=True)]