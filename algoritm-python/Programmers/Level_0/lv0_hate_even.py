#프로그래머스 lv.0, 짝수는 싫어요
def solution(n):
    return [x for x in range(1, n+1) if x % 2 == 1]