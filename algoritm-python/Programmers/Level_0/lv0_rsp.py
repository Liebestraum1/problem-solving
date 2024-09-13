#Programmers lv.0, 가위 바위 보
def solution(rsp):
    table = str.maketrans("025", "502")
    return rsp.translate(table)