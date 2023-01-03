def solution(clothes):
    dic = {}
    answer = 1
    for v, k in clothes:
        dic[k] = dic.get(k, 0) + 1

    for i in dic.values():
        answer *= (i + 1)
    return answer - 1