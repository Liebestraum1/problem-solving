#Programmer lv.2, 점 찍기
def solution(k, d):
    cnt = d//k + 1 # x축, 원점
    for x in range(0, d, k):
        cnt += ((d**2 - x**2) ** 0.5) // k
    return cnt