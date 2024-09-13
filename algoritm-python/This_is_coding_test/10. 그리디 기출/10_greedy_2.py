#0일때는 더한다
#1일때는 더한다
s = input()
answer = 0

for i in s:
    if i == '0' or i == '1':
        answer += int(i)
    elif answer < 2:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)
