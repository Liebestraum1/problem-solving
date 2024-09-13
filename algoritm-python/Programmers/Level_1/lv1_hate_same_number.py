#Programmers lv.1, 같은 숫자는 싫어
def solution(arr):
    answer = []
    stack = -1
    for i in arr:
        if i != stack:
            answer.append(i)
            stack = i
    return answer