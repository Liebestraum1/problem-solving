#Programmers lv.0, 다음에 올 숫자
def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] / common[0])