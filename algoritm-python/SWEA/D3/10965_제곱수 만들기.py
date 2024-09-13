pn = set(range(2, int((10 ** 7) ** 0.5) + 1))
for i in range(2, int((10 ** 7) ** 0.5) + 1):
    pn -= set(range(2 * i, int((10 ** 7) ** 0.5) + 1, i))

answers = []

t = int(input())
for test in range(1, t+1):
    a = int(input())
    answer = 1
    for divisor in pn:
        cnt = 0
        while a % divisor == 0:
            cnt += 1
            a //= divisor
        if cnt % 2 != 0:
            answer *= divisor
        if a == 1 or divisor >= int(a ** 0.5) + 1:
            break
    if a > 1:
        answer *= a
    answers.append(f"#{test} {answer}")

print(*answers, sep='\n')