t = int(input())

for test in range (1, t+1):
    l, u, x = map(int, input().split())
    if x > u:
        print(f"#{test} -1")
    elif x >= l and x <= u:
        print(f"#{test} 0")
    else:
        print(f"#{test} {l - x}")