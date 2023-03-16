def solution(relation):
    from itertools import combinations
    attribute = list(zip(*relation))
    answer = []
    
    for i in range(len(attribute)+1):
        for comb in combinations(range(len(attribute)), i):
            if len(set(zip(*[attribute[j] for j in comb]))) == len(relation):
                answer.append(comb)

    for i in range(len(answer)):
        if answer[i]:
            for j in range(i+1, len(answer)):
                if answer[j] and set(answer[i]) & set(answer[j]) == set(answer[i]):
                    answer[j] = False
    return len(answer) - answer.count(False)