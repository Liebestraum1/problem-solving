import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
visited = [False] * (n+1)
answer = [0] * (n+1)
order = 0
graph = {k : [] for k in range(1, n+1)}

for i in range(m):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    graph[edge].append(node)

for key in graph.keys():
    graph[key].sort()

def dfs(graph, start=r):
    global order
    order += 1
    visited[start] = True
    answer[start] = order
    for adjacent_node in graph[start]:
        if not visited[adjacent_node]:
            dfs(graph, adjacent_node)
    return

dfs(graph)
for i in answer[1:]:
    print(i)