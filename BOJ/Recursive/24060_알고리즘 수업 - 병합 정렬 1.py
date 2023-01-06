import sys
# import random
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

# data = []
# for i in range(500000):
#     data.append(random.randint(1, 500000))
# k = 15

count = 0
answer = 0
def merge_sort(a, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r): #p 시작점, q는 중간점, r은 끝나는 점
    global k, answer
    i = p; j = q + 1; t = 0 #i는 시작점, j는 중간점 + 1
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            t += 1; i += 1
        else:
            tmp[t] = a[j]
            t += 1; j += 1
    while i <= q:
        tmp[t] = a[i]
        t += 1; i += 1
    while j <= r:
        tmp[t] = a[j]
        t += 1; j += 1
    i = p; t = 0
    while i <= r:
        k -= 1
        if k == 0:
            answer = tmp[t]
            print(answer)
            exit()
        a[i] = tmp[t]
        i += 1; t += 1

merge_sort(data, 0, len(data)-1)
print(-1)