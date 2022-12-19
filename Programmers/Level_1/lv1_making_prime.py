#Programmers lv.1, 소수 만들기
from itertools import combinations
def solution(nums):
    def prime(a):
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True
    return len([True for i in combinations(nums, 3) if prime(sum(i)) == True])