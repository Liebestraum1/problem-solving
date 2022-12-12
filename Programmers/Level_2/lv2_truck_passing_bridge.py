def solution(bridge_length, weight, truck_weights):
    q = [1]
    q_times = [bridge_length]
    answer = 0
    
    while q:
        answer += 1
        for i in range(len(q_times)):
            q_times[i] += 1
        if q_times[0] == bridge_length + 1:
            q.pop(0)
            q_times.pop(0)
        if truck_weights:
            if len(q) < bridge_length and sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
                q_times.append(1)
    return answer