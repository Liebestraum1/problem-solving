import sys
input = sys.stdin.readline
n = int(input())
data = set()

for _ in range(n):
    people = input().split()[0]
    if people in data:
        data.remove(people)
    else:
        data.add(people)

print(*sorted(list(data), reverse = True), sep='\n')