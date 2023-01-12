#그리디 4. 1이 될 때 까지
n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k != 0:
        n -= 1
    else:
        n /= k
    count += 1

print(count)