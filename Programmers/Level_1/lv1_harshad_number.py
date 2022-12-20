#Programmers lv.1, 하샤드 수
def solution(x):
    return True if x % sum([int(i) for i in list(str(x))]) == 0 else False 