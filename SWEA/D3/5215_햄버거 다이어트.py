t = int(input())
for test in range(1, t+1):
    n, l = map(int, input().split()) #l을 넘지 않으면서 가장 점수가 크게
    dp = [[0 for i in range(l+1)] for j in range(n+1)]
    ingredient = [(0, 0)]
    for i in range(n):
        ingredient.append(tuple(map(int, input().split())))
    for ing in range(1, n+1):
        for kcal in range(l+1):
            if ingredient[ing][1] <= kcal:
                dp[ing][kcal] = max(dp[ing - 1][kcal - ingredient[ing][1]] + ingredient[ing][0],
                                    dp[ing - 1][kcal])
            else:
                dp[ing][kcal] = dp[ing - 1][kcal]
    print(f"#{test} {dp[-1][-1]}")