#Hash
from itertools import accumulate

def solution(bell):
    coors_start = {}
    coors_end = {}
    for i, x in enumerate(accumulate[0] + [-1 if b == 1 else 1 for b in bell]):
        if x not in coors_start:
            coors_start[x] = i
        coors_end[x] = i
    return max(coors_end[x] - coors_start[x] for x in coors_end)

"""
line 7은 누적합을 나타낸다. 해당 리스트의 각 요소는 빨간색 방울이 몇 개 더 많았는지 나타낸다.
어떤 요소의 값이 -1이면 해당 위치까지 빨간색 방울이 1개 더 많았다는 뜻.
요소의 값이 같은 지점끼리 자르면 빨간색 방울과 초록색 방울의 수가 동일하다는 뜻이다.

coors_start[x]는 최초로 빨간색 방울이 -x개 더 많았던 지점을 나타내는 hash table이다.
coors_end[x]는 빨간색 방울이 -x개 더 많은 지점을 누적합 리스트를 순회하며 갱신하는 hash table이다.
"""