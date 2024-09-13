def solution(begin, end):
    answer = [0] * (end - begin + 1)
    def cd(num):
        if num == 0:
            return 0
        divisor, share = 1, 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisor, share = i, num//i
                if share <= 10000000:
                    return share
        return divisor
    
    for i in range(len(answer)):
        if i + begin == 1:
            answer[i] = 0
        else:
            answer[i] = cd(i + begin)
    return answer