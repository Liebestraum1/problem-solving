t = int(input())
for test in range(1, t+1):
    start, end = map(int, input().split())
    print(f"#{test} {(start + end) % 24}")