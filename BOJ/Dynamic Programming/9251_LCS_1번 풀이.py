first_string = input()
second_string = input()

dp = [[0 for col in range(len(first_string) + 1)] for row in range(len(second_string) + 1)]
#first_string의 문자는 col, second_string의 문자는 row

for row in range(1, len(second_string)+1):
    for col in range(1, len(first_string)+1):
        if first_string[row-1] == second_string[col-1]:
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1])

print(dp[-1][-1])
