#Programmers lv.2, 교점에 별 만들기
from itertools import combinations

def solution(line):
    node = []
    for l1, l2 in combinations(line, 2):
        if l1[0] * l2[1] - l1[1] * l2[0] != 0:
            x = (l1[1] * l2[2] - l1[2] * l2[1]) / (l1[0] * l2[1] - l1[1] * l2[0])
            y = (l1[2] * l2[0] - l1[0] * l2[2]) / (l1[0] * l2[1] - l1[1] * l2[0])
        if int(x) == x and int(y) == y:
            node.append([x, y])
    min_x = -min(node, key = lambda x: x[0])[0]
    min_y = -min(node, key = lambda x: x[1])[1]
    node = [[int(x + min_x), int(y + min_y)] for x, y in node]
    base = (max(node, key = lambda x: x[0])[0]+1) #최대 x좌표
    height = (max(node, key = lambda x: x[1])[1]+1) #최대 y좌표
    
    answer = [['.' for x in range(base)] for y in range(height)]
    for base, height in node:
        answer[height][base] = '*'
    answer = [''.join(x) for x in answer]
    return answer[::-1]