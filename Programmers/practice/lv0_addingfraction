def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1*num2

    def mcd(a):
        cd = []
        for i in range(1, int(a**0.5)+1):
            if a % i == 0:
                cd.append(i)
                cd.append(a//i)
            if i == a//i:
                cd.pop()
        return(cd)

    x = max(set(mcd(denum))&set(mcd(num)))
    print(mcd(num))
    return [denum//x, num//x]