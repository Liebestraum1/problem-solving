n = int(input())
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

data = list(map(int, input().split()))
for num in data[1:]:
    print(f'{data[0]//gcd(data[0], num)}/{num//gcd(data[0], num)}')