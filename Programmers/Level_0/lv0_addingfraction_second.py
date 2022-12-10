#Programmers lv.0, 분수의 덧셈 2번 풀이
def solution(denum1, num1, denum2, num2):

    denum = (denum1*num2) +(denum2*num1)
    num = num1*num2

    for cd in range(min(denum,num), 0, -1):
        if denum % cd == 0 and num % cd == 0:
            gcd = cd
            break

    return [denum / gcd, num / gcd]
