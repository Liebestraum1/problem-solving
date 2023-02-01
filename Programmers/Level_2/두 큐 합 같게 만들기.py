from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1s, q2s = sum(queue1), sum(queue2)
    goal, count = (q1s + q2s) / 2, 0
    while count <= (len(queue1) + len(queue2)) * 2:
        if q1s == goal:
            return count
        if q1s < goal:
            k = q2.popleft()
            q1s += k
            q1.append(k)
        elif q1s > goal:
            k = q1.popleft()
            q1s -= k
            q2.append(k)
        count += 1
    return -1

#해설: https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/