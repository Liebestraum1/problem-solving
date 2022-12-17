#Programmers lv.1, 체육복
def solution(n, lost, reserve):
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]
    for i, v in enumerate(_reserve):
        if v-1 in _lost:
            _lost.remove(v-1)
        elif v+1 in _lost:
            _lost.remove(v+1)
    return n - len(_lost)