s1 = input()
s2 = input()

dp = []

for i in range(len(s2)):
    if s2[i] == s1[0]:
        dp.append((i, 1))

for a in s1[1:]:
    print(dp)
    for idx, b in enumerate(s2):
        if a == b:
            if min(dp, key = lambda x: x[0])[0] > idx:
                dp.append((idx, 1))
            else:
                for i in range(len(dp)):
                    if dp[i][0] < idx:
                        dp[i] = (idx, dp[i][1] + 1)
            break
print(dp)