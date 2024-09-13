n = int(input())
data_1 = list(map(int, input().split()))

m = int(input())
data_2 = list(map(int, input().split()))

data_1.sort()

for num in data_2:
    start, end = 0, n - 1
    while True:
        if start > end:
            print(0)
            break
        mid = (start + end) // 2
        if data_1[mid] == num:
            print(1)
            break
        elif data_1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1