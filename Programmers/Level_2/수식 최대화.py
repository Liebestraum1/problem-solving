from itertools import permutations
def solution(expression):
    answer = []
    def change(s, sign):
        k = s.split(sign[0])
        for i in range(len(k)):
            k[i] = str(eval(sign[1].join([str(eval(j)) for j in k[i].split(sign[1])])))
        return abs(eval(sign[0].join(k)))    
    for sign in permutations(['+', '-', '*'], 2):
        answer.append(change(expression, sign))
    return max(answer)