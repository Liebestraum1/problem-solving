n = int(input())
data = []
answer_list = []

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

for _ in range(n):
    data.append(int(input()))

data.sort()
data = [data[i] - data[i-1] for i in range(1, n)]

answer = data[0]
for i in range(1, n-1):
    answer = gcd(answer, data[i])

for d in range(1, int(answer ** 0.5 + 1)):
    if answer % d == 0:
        answer_list.append(d)
        if d != answer // d:
            answer_list.append(answer // d)

print(*sorted(answer_list)[1:], sep='\n')