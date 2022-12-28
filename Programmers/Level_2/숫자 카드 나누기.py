def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]

    def gcd(num1, num2):
        r = num2 % num1
        if r == 0:
            return num1
        return gcd(r, num1)

    for i in arrayA:
        gcdA = gcd(gcdA, i)
    for j in arrayB:
        gcdB = gcd(gcdB, j)

    for a in arrayA:
        if a % gcdB == 0:
            gcdB = 0
            break

    return max(gcdA, gcdB)