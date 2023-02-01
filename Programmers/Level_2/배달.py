def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    answer = [0, 1] + [0 for _ in range(N+1)]
    for start, end, time in road:
        graph[start].append((end, time))
        graph[end].append((start, time))
    
    def dfs(graph, start=1, t=0):
        for d, time in graph[start]:
            if answer[d] and t + time >= answer[d]:
                continue
            elif t+time <= K:
                answer[d] = t + time
                dfs(graph, d, t+time)
    dfs(graph)
    return len([i for i in answer if i > 0])