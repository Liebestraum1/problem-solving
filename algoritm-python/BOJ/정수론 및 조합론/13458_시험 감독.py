n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for test in a:
    answer += 1
    test -= b
    if test > 0:
        if test % c == 0:
            answer += test // c
        else:
            answer += test // c + 1
print(answer)