n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))

answer = 0
end_time = 0

time.sort(key = lambda x: (x[1], x[0])) #끝나는 시간 순 정렬
for i in time:
    if i[0] >= end_time:
        answer += 1
        end_time = i[1]

print(answer)