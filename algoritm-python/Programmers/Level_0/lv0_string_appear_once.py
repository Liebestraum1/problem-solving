#Programmers lv.0, 한 번만 등장한 문자
def solution(s):
    answer = ""
    dic = dict.fromkeys(s, 0)
    for i in s:
        dic[i] += 1
    for string, cnt in dic.items():
        if cnt == 1:
            answer += string
    return ''.join(sorted(answer))