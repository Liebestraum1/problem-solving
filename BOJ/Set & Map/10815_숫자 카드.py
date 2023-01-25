n = int(input())
data = set(map(int, input().split()))
m = int(input())
key = list(map(int, input().split()))

for k in key:
    if k in data:
        print(1, end=' ')
    else:
        print(0, end=' ')