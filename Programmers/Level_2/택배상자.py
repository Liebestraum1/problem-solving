from collections import deque
def solution(order):
    answer = 0
    q = deque([i for i in range(1, len(order)+1)])
    stack = []
    for o in order:
        print(q, stack)
        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
        else:
            while q and q[0] != o:
                stack.append(q.popleft())
            if not q:
                break
            else:
                q.popleft()
                answer += 1
    return answer