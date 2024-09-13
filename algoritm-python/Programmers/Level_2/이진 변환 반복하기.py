def solution(s): #format 함수 사용
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        num = 0
        for i in s:
            if i == '1':
                num += 1
            else:
                answer[1] += 1
        
        s = ''
        while num > 0:
            s += str(num % 2)
            num //= 2
        s = s[::-1]
        
    return answer

def solution(s): #format 함수 사용 x (이진수 변환 직접 구현)
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        num = 0
        for i in s:
            if i == '1':
                num += 1
            else:
                answer[1] += 1
        
        s = ''
        while num > 0:
            s += str(num % 2)
            num //= 2
        s = s[::-1]
        
    return answer