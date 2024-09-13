side = int(input())
data = []
answer = []

for row in range(side):
    data.append(list(map(int, input())))

def divide(arr):
    if sum(map(sum, arr)) == 0:        
        answer.append('0')
        return
    elif sum(map(sum, arr)) == len(arr) * len(arr):
        answer.append('1')
        return
    else:
        answer.append('(')
        divide(list(zip(*list(zip(*arr[:len(arr)//2]))[:len(arr)//2])))
        divide(list(zip(*list(zip(*arr[:len(arr)//2]))[len(arr)//2:])))
        divide(list(zip(*list(zip(*arr[len(arr)//2:]))[:len(arr)//2])))
        divide(list(zip(*list(zip(*arr[len(arr)//2:]))[len(arr)//2:])))
        answer.append(')')

divide(data)
print(''.join(answer))