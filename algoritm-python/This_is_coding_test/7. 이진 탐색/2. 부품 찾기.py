n = int(input())
data = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

data.sort()

def bs(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return bs(array, target, start, mid-1)
    else:
        return bs(array, target, mid + 1, end)

for r in request:
    if bs(data, r, 0, n - 1):
        print("yes")
    else:
        print("no")