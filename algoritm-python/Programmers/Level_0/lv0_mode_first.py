#Programmers lv.0, 최빈값 구하기 1번 풀이

#해시 사용
def solution(array):
    answer = {}
    for i in array:
        answer[i] = answer.get(i,0) + 1
    freq = [k for k, v in answer.items() if max(answer.values()) == v]
    return (-1 if len(freq) > 1 else freq[0])
