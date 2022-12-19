#Programmers lv.1, 삼총사
from itertools import combinations
def solution(number):
    answer = [sum(i) for i in combinations(number, 3)]
    return answer.count(0)