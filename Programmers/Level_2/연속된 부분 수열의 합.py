def solution(sequence, k):
    answer = []
    prefix_sum = [0 for _ in range(len(sequence) + 1)]
    for i in range(len(sequence)):
        prefix_sum[i+1] = prefix_sum[i] + sequence[i]
    
    start = 0
    for end in range(1, len(prefix_sum)):
        while prefix_sum[end] - prefix_sum[start] > k:
            start += 1
        if prefix_sum[end] - prefix_sum[start] == k:
            answer.append([start, end-1])
    return min(answer, key = lambda x: (x[1] - x[0], x[0]))