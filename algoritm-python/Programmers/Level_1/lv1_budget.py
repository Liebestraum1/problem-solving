#Programmers lv.1, 예산
def solution(d, budget):
    for i, v in enumerate(sorted(d)):
        if budget < v:
            return i
        else:
            budget -= v
    return i+1