from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        dic = {}
        for o in orders:
            cnt = 0
            for comb in combinations(sorted(o), i):
                dic[comb] = dic.get(comb, 0) + 1
        dic = {key : value for key, value in dic.items() if value > 1}
        dic = [''.join(key) for key, value in dic.items() if value == max(dic.values())]
        if dic:
            answer += dic
    return sorted(answer)