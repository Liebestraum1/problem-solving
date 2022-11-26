def solution(n, lost, reserve):
    overlap = set(reserve) & set(lost)
    reserve = set(reserve) - overlap
    lost = set(lost) - overlap
    
    for i in sorted(reserve):
        if i - 1 in lost:
            lost.remove(i-1)
        elif i + 1 in lost:
            lost.remove(i+1)
    return n - len(lost)