data = []
n, m = map(int, input().split())
cha = list(map(int, input().split())) #0, 1은 현재 위치의 n[세로], m[가로]좌표, 2는 방향
for i in range(n):
    data.append(list(map(int, input().split())))


visited = [[cha[0], cha[1]]] #방문한 칸의 리스트
rotate = 0
#회전 방향 = 0(북) -> 3(서) -> 2(남) -> 1(동)
#캐릭터 위치 [a][b]에서 북은 a+1, 서는 b-1, 남은 a-1, 동은 b+1
    
def move(direction):
    if direction[2] == 0:
        return [direction[0]+1, direction[1]]
    if direction[2] == 1:
        return [direction[0], direction[1]+1]
    if direction[2] == 2:
        return [direction[0]-1, direction[1]]
    if direction[2] == 3:
        return [direction[0], direction[1]-1]
    
def reverse_move(direction):
    if direction[2] == 0:
        return [direction[0]-1, direction[1]]
    if direction[2] == 1:
        return [direction[0], direction[1]-1]
    if direction[2] == 2:
        return [direction[0]+1, direction[1]]
    if direction[2] == 3:
        return [direction[0], direction[1]+1]

#회전하는 식
while True:
    cha[2] = (abs(cha[2] - 1)) % 4
    rotate += 1
    if move(cha)[0] >= n or move(cha)[1] >= m or move(cha) in visited or data[move(cha)[0]][move(cha)[1]] == 1:
        if rotate == 4:
            cha = reverse_move(cha) + [cha[2]]
            rotate = 0
            if data[cha[0]][cha[1]] == 1:
                break
        continue
    visited.append(move(cha))
    cha = move(cha) + [cha[2]]
    rotate = 0

print(len(visited))