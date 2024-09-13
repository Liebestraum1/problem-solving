def solution(tickets):
    visited = ['ICN']
    node = 'ICN' #현재 위치
    route = {i : [] for i, v in tickets}

    for i, v in tickets:
        route[i].append(v)
    
    while route:
        for i in sorted(route[node]):
            next = i
            if i in route.keys():
                if set(route[i]) != {i}:
                    next = i
                    break
        route[node].remove(next)
        if route[node] == []: 
            route.pop(node)
        node = next
        visited.append(node)

    return visited
