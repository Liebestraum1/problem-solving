t = int(input())

def dfs(start, visited, depth):
    for end in graph[start]:
        if end not in visited:
            visited.append(end)
            dfs(end, visited, depth + 1)
            visited.pop()
        else:
            answer.append(depth)

for test in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    answer = [1]
    for i in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    for root in range(1, n+1):
        v = [root]
        dfs(root, v, 1)
    print(f"#{test} {max(answer)}")