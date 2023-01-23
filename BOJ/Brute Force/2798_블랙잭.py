import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
print(max([i for i in map(sum, combinations(data, 3)) if i <= m]))