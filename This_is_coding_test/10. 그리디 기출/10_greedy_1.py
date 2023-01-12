#그 그룹의 최대 공포도가 X이면 그 그룹의 인원수는 X명 이상이어야 함.
#
n = int(input())
data = list(map(int, input().split()))
group = []
answer = 0
#공포도가 낮은 순서대로 구성할 것.
#1. 오름차 순으로 정렬한다.
#2. data를 조회하면서 group에 한명씩 append
#3. group의 마지막 값과 길이가 동일해지면 answer에 1을 더하고 리스트를 초기화한다.

data.sort()
for i in range(n):
    group.append(data[i])
    if group[-1] == len(group):
        answer += 1
        group = []

print(answer)