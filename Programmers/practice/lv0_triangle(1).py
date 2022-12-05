def solution(sides):
    if max(sides) >= sum(sides) - max(sides):
        return 2
    return 1