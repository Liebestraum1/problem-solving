from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
    return answer if scoville[0] >= K else -1