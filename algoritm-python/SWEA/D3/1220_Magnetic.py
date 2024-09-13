for test in range(1, 11):
    side = int(input())
    answer = 0
    stack = [0 for _ in range(side)]
    for row in range(100):
        data = list(map(int, input().split()))
        for magnet in range(100):
            if data[magnet] == 1:
                stack[magnet] = 1
            elif data[magnet] == 2 and stack[magnet]:
                answer += stack[magnet]
                stack[magnet] = 0
    print(f"#{test} {answer}")