def solution(n, k):
    def prime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True if num > 1 else False

    answer = 0
    convert = ''
    
    while n >= k:
        convert += str(n % k)
        n //= k
        if n < k:
            convert += str(n)
            
    convert = [int(i) for i in convert[::-1].split('0') if i.isdigit()]
    
    for i in convert:
        if prime(i):
            answer += 1
    return answer