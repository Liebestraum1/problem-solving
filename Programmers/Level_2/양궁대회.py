def solution(n, info):
    visited = []
    gap = 0
    answer = []
    def dfs(target, arrow, last):
        nonlocal gap
        nonlocal answer
        for shot in range(last, 11):
            if target[shot] < arrow and shot not in visited:
                visited.append(shot)
                dfs(target[:shot] + [-1] + target[shot+1:], arrow - (target[shot]+1), shot)
                visited.pop()
            elif shot == 10:
                result = 0
                if info != target:
                    target[shot] -= arrow
                for score in range(11):
                    if target[score] == -1:
                        result += 10 - score
                    elif target[score] > 0:
                        result -= 10 - score
                if result > gap:
                    gap = result
                    answer = [target]
                elif result == gap:
                    answer.append(target)
                return
    dfs(info, n, 0)
    answer.sort(key = lambda x : x[::-1], reverse=True)
    
    return [-1] if gap == 0 else [info[i] - answer[-1][i] for i in range(11)]