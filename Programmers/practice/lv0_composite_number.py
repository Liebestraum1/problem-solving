#Programmers lv.0, 합성수 찾기
def solution(n):
    composite = set()
    for k in range(2, int(n**0.5)+1):
        composite = composite | {b for b in range (k*2, n+1, k)}
    return len(composite)