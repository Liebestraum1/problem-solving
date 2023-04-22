def solution(targets):
    targets.sort(key = lambda x: (x[0], x[1]))
    start, end = -1, -1
    answer = 0

    for target_start, target_end in targets:
        if target_start < end and target_end <= end:
            start = target_start
            end = target_end
        elif target_start < end and target_end >= end:
            start = target_start
        else:
            answer += 1
            start = target_start
            end = target_end
    return answer