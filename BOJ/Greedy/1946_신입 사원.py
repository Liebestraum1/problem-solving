import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    data = [0] * (n+1)
    answer = 0
    interview_rank = n+1
    
    for _ in range(n):
        portfolio, interview = map(int, sys.stdin.readline().split())
        data[portfolio] = interview
    
    for rank in data[1:]:
        if rank < interview_rank:
            answer += 1
            interview_rank = rank
    print(answer)