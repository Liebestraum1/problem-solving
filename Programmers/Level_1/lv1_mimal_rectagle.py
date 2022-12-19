#Programmers lv.1, 최소직사각형
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)