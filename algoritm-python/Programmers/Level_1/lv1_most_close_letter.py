#Programmers lv.1, 가장 가까운 같은 글자
def solution(s):
    dic = dict()
    answer = []
    
    for i, v in enumerate(s):
        if v not in dic: 
            answer.append(-1)
            dic[v] = i
        else:
            answer.append(i - dic[v])
            dic[v] = i
    return answer