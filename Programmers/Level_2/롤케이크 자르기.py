def solution(topping):
    left, right = {}, set()
    answer = 0
    for t in topping:
        left[t] = left.get(t, 0) + 1
    while topping:
        t = topping.pop()
        left[t] -= 1; right.add(t)
        if left[t] == 0:
            left.pop(t)
        if len(left) == len(right):
            answer += 1
    return answer