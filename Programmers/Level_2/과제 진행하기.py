def solution(plans):
    answer = [] #정답 리스트
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2]) * 60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x: x[1], reverse=True)
    
    name, start, time = plans.pop() #과목명, 시작시간, 소요시간
    remain = []
    
    while plans:
        nn, ns, nt = plans.pop() #시작할 때가 된 과목의 시간
        if start + time <= ns:
            answer.append(name)
            time_left = ns - (start + time) #남은 시간
            while time_left and remain:
                if remain[-1][1] <= time_left:
                    time_left -= remain[-1][1]
                    answer.append(remain.pop()[0])
                else:
                    remain[-1][1] -= time_left
                    time_left = 0
        else:
            remain.append([name, start + time - ns])
        name, start, time = nn, ns, nt
    
    remain.append([name, start])
    while remain:
        answer.append(remain.pop()[0])
    
    return answer