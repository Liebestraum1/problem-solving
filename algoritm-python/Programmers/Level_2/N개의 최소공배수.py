def solution(arr):
    def lcm(a, b):
        def gcd(num1, num2):
            if num1 % num2 == 0:
                return num2
            return gcd(num2, num1%num2)
        return (a * b) / gcd(a, b)
    
    answer = 1
    for i in arr:
        answer = lcm(answer, i)
    return answer