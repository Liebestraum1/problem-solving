#Programmers lv.1, 기사단원의 무기
def solution(number, limit, power):
    def number_of_divisor(n):
        result = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                result += 2
                if n // i == i:
                    result -= 1
        return result
    
    iron = [number_of_divisor(i) if number_of_divisor(i) <= limit else power for i in range(1, number+1)]
    return sum(iron)