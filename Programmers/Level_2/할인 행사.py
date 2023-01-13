def solution(want, number, discount):
    answer = 0
    j = {want[i] : number[i] for i in range(len(want))}
    for i in range(len(discount) - 9):
        d = {}
        for i in discount[i:i+10]:
            d[i] = d.get(i, 0) + 1
        if j == d:
            answer += 1
    return answer