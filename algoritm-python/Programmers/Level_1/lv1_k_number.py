#Programmers lv.1, K번째 수
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]