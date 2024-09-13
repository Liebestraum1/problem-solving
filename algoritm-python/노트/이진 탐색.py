#재귀
def bs(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bs(array, target, start, mid-1)
    else:
        return bs(array, target, mid+1, end)

print(bs([1,2,3,4,5,6], 4, 0, 5))