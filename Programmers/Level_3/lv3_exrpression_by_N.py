#Programmers lv.3, N으로 표현
def solution(N, number):
    answer = []
    
    def arithmetic(iter, k):
        a = []
        for i in iter:
            a.append(k + i)
            a.append(k - i)
            if i != 0:
                a.append(i * k)
                a.append(i // k)
        return a
    
    def decimal(a, b):
        c = 0
        for i in range(b+1):
            c += a * (10 ** i)
        return c

    for i in range(8):
        answer.append([decimal(N, i)])
        for j in range(i):
            answer[i].extend(arithmetic(answer[j], decimal(N, i-j-1)))
        answer[i] = list(set(answer[i]))
        if number in answer[i]:
            return i+1
    return -1