#Programmers lv.0, 직사각형의 넓이 구하기
def solution(dots):
    height = max(dots, key=lambda x: x[1])[1] - min(dots, key=lambda x: x[1])[1]
    width = max(dots, key=lambda x:x[0])[0] - min(dots, key=lambda x: x[0])[0]
    return abs(height * width)