#Programmers lv.2, 우박수열 정적분
def solution(k, ranges):
    height = [k]
    result = []
    while k != 1:
        if k % 2 == 0:
            k = k // 2
            height.append(k)
        else:
            k = k * 3 + 1
            height.append(k) #수열 구하는 부분


    def integral(l, area=0.0): #ranges를 받는다
        if len(l) == 1:
            return area
        return integral(l[1:], area + (l[0] + l[1]) * 0.5)
#ing
