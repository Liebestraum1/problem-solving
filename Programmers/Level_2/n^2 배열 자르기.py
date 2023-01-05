def solution(n, left, right): #처음 풀이
    a = [i+1 for i in range(n)] #굳이 초기화 할 필요 없음
    answer = []

    for i in range(left, right+1):
        if i % n > i // n:
            answer.append(a[i%n])
        else:
            answer.append(a[i//n])
    return answer


def solution(n, left, right): #몫이 크면 몫이 행렬로, 나머지가 크면 나머지가 행렬로 
    answer = [] 
    for i in range(left, right+1):
        answer.append(max(divmod(i, n)) + 1)
    return answer