n = int(input())

def func(k, answer):
    if k == 0:
        return answer
    return func(k // 10, answer + k % 10)

print(func(n, 0))