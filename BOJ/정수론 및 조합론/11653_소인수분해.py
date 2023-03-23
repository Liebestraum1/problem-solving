n = int(input())
if n > 1:
    for i in range(2, n+1):
        while n % i == 0:
            n //= i
            print(i)
        if n == 1:
            break