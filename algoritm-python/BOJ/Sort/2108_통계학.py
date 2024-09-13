import sys
input = sys.stdin.readline

n = int(input())
data = []
cnt = {}
for _ in range(n):
    data.append(int(input()))

data.sort()
for i in data:
    cnt[i] = cnt.get(i, 0) + 1
f = [key for key in cnt if cnt[key] == max(cnt.values())]

print(round(sum(data) / len(data)))
print(data[len(data)//2])
print(f[0] if len(f) == 1 else f[1])
print(max(data) - min(data))