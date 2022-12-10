#Programmers lv.0, 점의 위치 구하기
def solution(dot):
    if dot[0] < 0:
        if dot[1] < 0:
            return 3
        else:
            return 2
    elif dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4