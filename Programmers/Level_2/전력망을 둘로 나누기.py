def solution(n, wires):
    from collections import deque
    graph = {node : [] for node in range(1, n+1)}
    answer = 100

    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    for start in graph:
        for cut in graph[start]:
            linked = 0
            queue = deque([start])
            visited = [False for _ in range(n+1)]
            visited[start], visited[cut] = True, True
            while queue:
                v = queue.popleft()
                linked += 1
                for i in graph[v]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
            answer = min(answer, abs(2 * linked - n))
    return answer