import sys
from itertools import combinations
input = sys.stdin.readline
people = [i for i in range(int(input()))]
score = []
answer = [] 

for i in range(len(people)):
    score.append(list(map(int, input().split())))

for team in combinations(people, len(people)//2):
    stat = 0
    start = team
    link = [p for p in people if p not in start]
    for p1, p2 in combinations(start, 2):
        stat += score[p1][p2] + score[p2][p1]
    for p1, p2 in combinations(link, 2):
        stat -= score[p1][p2] + score[p2][p1]
    answer.append(abs(stat))

print(min(answer))