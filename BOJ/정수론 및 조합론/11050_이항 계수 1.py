n, k = map(int, input().split())
def f(num):
    answer  = 1
    if num < 2:
        return answer
    for i in range(2, num+1):
        answer *= i
    return answer

print(int(f(n) / (f(k) * f(n-k))))