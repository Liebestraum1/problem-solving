from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        data = i.split()
        for r in range(5):
            for key in combinations(data, r):
                dic[key].append(int(data[-1]))
    
    for value in dic.values():
        value.sort()
    
    for q in query:
        condition = q.replace('and', '').replace('-', '').split()
        key, score = tuple(condition[:-1]), int(condition[-1])
        result = 0

        if key in dic:
            idx = bisect_left(dic[key], score)
            result = len(dic[key]) - idx
        answer.append(result)
    return answer