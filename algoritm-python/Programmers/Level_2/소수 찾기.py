from itertools import permutations
def pn(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    data = []
    for i in range(1, len(numbers)+1):
        data.extend(map(lambda x: int(''.join(x)), permutations(numbers, i)))
    for i in set(data):
        if pn(i):
            answer += 1
    return answer