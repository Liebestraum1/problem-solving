#구현 2. 시각
n = int(input())
count = 0

# 내 풀이
# for i in range((n+1)* 60 * 60):
#     if '3' in str(i // 3600).zfill(2) + str(i // 60 % 60).zfill(2) + str(i % 60).zfill(2):
#         count += 1
        
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)