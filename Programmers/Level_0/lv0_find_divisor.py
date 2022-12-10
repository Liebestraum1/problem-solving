#Programmers lv.0, 약수 구하기
def solution(n):
    answer = []
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            answer.extend([i, n//i])
    return sorted(list(set(answer)))