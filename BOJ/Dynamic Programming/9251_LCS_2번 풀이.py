first_string = input()
second_string = input()

#sol 2
dp = [0 for _ in range(len(second_string))]
for i in range(len(first_string)):
    cnt = 0
    for j in range(len(second_string)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif first_string[i] == second_string[j]:
            dp[j] = cnt + 1

print(max(dp))