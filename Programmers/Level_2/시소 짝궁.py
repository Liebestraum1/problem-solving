def solution(weights):
    answer = 0
    dic = {}
    for weight in sorted(weights):
        dic[weight] = dic.get(weight, 0) + 1

    for key, value in dic.items():
        answer += value * (value - 1) // 2
        if int(key * 1.5) == key * 1.5 and key * 1.5 in dic:
            answer += value * dic[key * 1.5]
        if int(key * 2) in dic:
            answer += value * dic[key * 2]
        if int(key / 3 * 4) == key / 3 * 4 and key / 3 * 4 in dic:
            answer += value * dic[key / 3 * 4]    
    return answer