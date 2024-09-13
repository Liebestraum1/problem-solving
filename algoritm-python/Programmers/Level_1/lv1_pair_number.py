#Programmers lv.1, 숫자 짝꿍
def solution(X, Y):
    result = ''
    xcnt = [0] * 10
    ycnt = [0] * 10
    
    for i in X:
        xcnt[int(i)] += 1
    for j in Y:
        ycnt[int(j)] += 1
    for k in range(9, -1, -1):
        if xcnt[k] <= ycnt[k]:
            result += str(k) * xcnt[k]
        else:
            result += str(k) * ycnt[k]
    
    if set(result) == {'0'}:
        return '0'
    elif result == '':
        return '-1'
    else:
        return result