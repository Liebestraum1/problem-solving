t = int(input())
for test in range(1, t+1):
    answer, now = 0, '0'
    
    data = input()
    for i in data:
        if now != i:
            now = i
            answer += 1
    
    print(f"#{test} {answer}")