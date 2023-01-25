n = int(input())
data = list(map(int, input().split()))
m = int(input())
key = list(map(int, input().split()))
dic = {}

for i in data:
    dic[i] = dic.get(i, 0) + 1

for k in key:
    if k not in dic:
        print(0, end=' ')
    else:
        print(dic[k], end=' ')