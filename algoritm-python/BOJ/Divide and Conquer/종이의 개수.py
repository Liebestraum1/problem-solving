side = int(input())
data = []
answer = [0, 0, 0] # -1, 0, 1

for row in range(side):
    data.append(list(map(int, input().split())))

def divide(arr):
    value = arr[0][0]
    if len(arr) == 1:
        answer[value + 1] += 1
    elif len(set([i for j in arr for i in j])) == 1:
        answer[value + 1] += 1
    else: #3등분 -> 피봇 -> 3등분
        divide(list(zip(*list(zip(*arr[:len(arr)//3]))[:len(arr)//3]))) # 1영역
        divide(list(zip(*list(zip(*arr[:len(arr)//3]))[len(arr)//3 : len(arr)//3 * 2]))) # 2영역
        divide(list(zip(*list(zip(*arr[:len(arr)//3]))[len(arr)//3 * 2:]))) # 3영역
        divide(list(zip(*list(zip(*arr[len(arr)//3:len(arr)//3 * 2]))[:len(arr)//3]))) # 4영역
        divide(list(zip(*list(zip(*arr[len(arr)//3:len(arr)//3 * 2]))[len(arr)//3 : len(arr)//3 * 2]))) # 5영역
        divide(list(zip(*list(zip(*arr[len(arr)//3:len(arr)//3 * 2]))[len(arr)//3 * 2:]))) # 6영역
        divide(list(zip(*list(zip(*arr[len(arr)//3 * 2:]))[:len(arr)//3]))) # 7영역
        divide(list(zip(*list(zip(*arr[len(arr)//3 * 2:]))[len(arr)//3 : len(arr)//3 * 2]))) # 8영역
        divide(list(zip(*list(zip(*arr[len(arr)//3 * 2:]))[len(arr)//3 * 2:]))) # 9영역

divide(data)
print(*answer, sep='\n')