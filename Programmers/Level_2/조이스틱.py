def solution(name):
    answer = 10000000
    alphabet = 0
    for string in name:
        alphabet += min(ord(string) - 65, 91 - ord(string))

    visited = [True if string == 'A' else False for string in name]
    visited[0] = True

    def dfs(idx, visited, result):
        nonlocal answer
        if set(visited) == {True}:
            answer = min(answer, result)
            return
        for i in range(1, len(visited)//2+1):
            a = (idx + i) % len(visited)
            if visited[a] == False:
                visited[a] = True
                dfs(a, visited, result + i)
                visited[a] = False
                break
        for i in range(1, len(visited)//2+1):
            if idx - i < 0:
                a = len(visited) + (idx - i)
            else:
                a = idx - i
            if visited[a] == False:
                visited[a] = True
                dfs(a, visited, result + i)
                visited[a] = False
                break
    dfs(0, visited, 0)
    return answer + alphabet