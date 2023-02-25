def solution(n, l, r):
    cnt = [0, 1, 2, 2, 3, 4]
    def dp(i, end):
        if i == 1:
            return cnt[end]
        qt, rm = divmod(end, 5 ** (i-1)) #몫, 나머지
        if qt == 2:
            return cnt[qt] * (4 ** (i-1))
        else:
            return cnt[qt] * (4 ** (i-1)) + dp(i-1, rm)
    return dp(n, r) - dp(n, l - 1)