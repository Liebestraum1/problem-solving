def solution(land):
    for i in range(len(land)-1):
        idx = land[i].index(max(land[i]))
        mv1 = land[i].pop(idx)
        mv2 = max(land[i])
        
        for j in range(4):
            if j != idx:
                land[i+1][j] += mv1
            else:
                land[i+1][j] += mv2
    return max(land[-1])