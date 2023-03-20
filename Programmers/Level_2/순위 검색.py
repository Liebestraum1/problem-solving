from itertools import combinations

def solution(info, query):
    answer = []
    dic = {() : []}
    for i in info:
        data = i.split()
        dic[()].append(int(data[-1]))
        for r in range(1, 5):
            for key in combinations(data, r):
                dic[key] = dic.get(key, []) + [int(data[-1])]
        
    for q in query:
        condition = q.replace('and', '').replace('-', '').split()
        key, score = tuple(condition[:-1]), int(condition[-1])
        result = 0

        if key in dic:
            for s in dic[key]:
                if s >= score:
                    result += 1
        answer.append(result)
    return answer