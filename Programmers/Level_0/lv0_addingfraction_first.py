#Programmers lv.0, 분수의 덧셈 1번 풀이
def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1*num2

    def divisor(n):
        divisor_list = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisor_list.append(i)
                divisor_list.append(n//i)
            if i == n//i:
                divisor_list.pop()
        return(divisor_list)

    gcd = max(set(divisor(denum))&set(divisor(num)))
    return [denum//gcd, num//gcd]