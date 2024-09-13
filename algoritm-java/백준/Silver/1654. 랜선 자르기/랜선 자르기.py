import sys
input = sys.stdin.readline

array = []
n, k = map(int, input().split())
for _ in range(n):
    array.append(int(input()))

start, end = 0, max(array)

while start <= end:
    cnt = 0 #잘린 랜선의 개수
    mid = (start + end) // 2
    if mid != 0:
        for a in array:
            cnt += a // mid
    else:
        cnt = sum(array)
    if cnt < k:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)