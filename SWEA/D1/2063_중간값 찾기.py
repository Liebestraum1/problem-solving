n = int(input())
data = sorted(list(map(int, input().split())))

print(data[(n-1)//2])