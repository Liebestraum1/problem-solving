def solution(s): #잘못 접근, k개로 자를 수 있는 경우 다 잘라버리는 경우
    answer = 1000
    for k in range(1, len(s)//2 + 1):
        idx, cnt, m = 0, 0, 0
        while idx <= len(s):
            if s[idx : k + idx] == s[k + idx : 2 * k + idx]:
                idx += k
                cnt += 1
            else:
                if cnt == 0:
                    m += 1
                    idx += 1
                else:
                    m += len(str(cnt+1)) + k
                    idx += k
                    cnt = 0
        answer = min(m, answer)
    return answer

def solution(s):
    answer = len(s)
    for k in range(1, len(s)//2 + 1):
        cnt, m = 0, 0
        for i in range(0, len(s), k):
            if s[i : k + i] == s[k + i : 2 * k + i]:
                cnt += 1
            else:
                if cnt == 0:
                    m += min(k, len(s) - i)
                else:
                    m += len(str(cnt+1)) + min(k, len(s) - i)
                    cnt = 0
        answer = min(m, answer)
    return answer