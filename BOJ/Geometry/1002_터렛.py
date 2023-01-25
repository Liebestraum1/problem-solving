n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2  + (y2 - y1) ** 2) ** 0.5 #두 원 중심거리
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif r1 + r2 < d:
        print(0)
    elif r1 + r2 == d:
        print(1)
    elif max(r1, r2) - min(r1, r2) < d and r1 + r2 > d:
        print(2)
    elif max(r1, r2) - min(r1, r2) == d:
        print(1)
    else:
        print(0)