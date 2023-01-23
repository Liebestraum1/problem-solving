n = int(input())
start = n - int(str(n)[0]) - ((len(str(n)) - 1) * 9)
while start < n:
    if start + sum(map(int, str(start))) == n:
        print(start)
        break
    start += 1
if start == n:
    print(0)