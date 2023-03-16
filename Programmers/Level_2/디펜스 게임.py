from heapq import heappush, heappop
def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        n -= enemy[i]
        heappush(heap, -enemy[i])
        if n < 0 and k == 0:
            return i
        elif n < 0 and k > 0:
            n += -heappop(heap)
            k -= 1
    return len(enemy)