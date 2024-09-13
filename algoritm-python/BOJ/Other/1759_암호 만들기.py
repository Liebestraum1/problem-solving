from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
data = input().split()
data.sort()

for password in combinations(data, l):
    count = 0
    for alphabet in password:
        if alphabet in 'aeiou':
            count += 1
    if count >= 1 and count <= l - 2 :
        print(''.join(password))