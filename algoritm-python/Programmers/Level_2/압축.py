def solution(msg):
    answer = []
    dic = {chr(i): i-64 for i in range(65, 91)}
    idx = 26
    pointer = 0
    
    for i in range(len(msg)):
        if i < pointer:
            continue
        pointer = len(msg)
        while msg[i:pointer] not in dic:
            pointer -= 1
        answer.append(dic[msg[i:pointer]])
        idx += 1
        dic[msg[i:pointer+1]] = idx
    
    return answer