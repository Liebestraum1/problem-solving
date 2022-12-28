import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = []

answer = 0

for i in range(n):
    data.append(int(input()))

heapq.heapify(data)

while len(data) > 1:
    card = heapq.heappop(data) + heapq.heappop(data)
    answer += card
    heapq.heappush(data, card)

print(answer)