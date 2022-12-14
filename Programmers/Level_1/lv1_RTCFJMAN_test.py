#Programmers lv.1, 성격 유형 검사하기
def solution(survey, choices):
    dic = {key : 0 for key in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}
    tp = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    answer = ''

    def score(a, b): #a는 선택지, b는 점수
        if b < 4:
            return (a[0], 4-b)
        elif b > 4:
            return (a[1], b-4)
        else:
            return (a[0], 0)

    for i, v in enumerate(survey):
        k = score(v, choices[i])
        dic[k[0]] += k[1]

    for t1, t2 in tp:
        if dic[t1] > dic[t2]:
            answer += t1
        elif dic[t1] < dic[t2]:
            answer += t2
        else:
            answer += min(t1, t2)

    return answer