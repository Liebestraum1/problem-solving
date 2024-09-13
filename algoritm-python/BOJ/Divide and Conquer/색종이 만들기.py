import sys
input = sys.stdin.readline

side = int(input())
data = []
answer = [0, 0] #white, blue

for row in range(side):
    data.append(list(map(int, input().split())))

def divide(arr):
    if sum(map(sum, arr)) == 0:        
        answer[0] += 1
        return
    elif sum(map(sum, arr)) == len(arr) * len(arr):
        answer[1] += 1
        return
    else:
        divide(list(zip(*list(zip(*arr[:len(arr)//2]))[:len(arr)//2])))
        divide(list(zip(*list(zip(*arr[:len(arr)//2]))[len(arr)//2:])))
        divide(list(zip(*list(zip(*arr[len(arr)//2:]))[:len(arr)//2])))
        divide(list(zip(*list(zip(*arr[len(arr)//2:]))[len(arr)//2:])))

divide(data)
print(*answer, sep='\n')