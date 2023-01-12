def solution(k, dungeons):
    answer = []
    def adventure(s, arr, n):
        if not arr:
            answer.append(n)
        for i in range(len(arr)):
            if s >= arr[i][0]:
                adventure(s - arr[i][1], arr[:i] + arr[i+1:], n+1)
            else:
                answer.append(n)
    adventure(k, dungeons, 0)
    return max(answer)