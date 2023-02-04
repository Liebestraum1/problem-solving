dic = {}
def f(num):
    if num in dic:
        return dic[num]
    if num < 4:
        return 1
    if num == 4 or num == 5:
        return 2
    dic[num] = f(num-1) + f(num-5)
    return dic[num]

t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))