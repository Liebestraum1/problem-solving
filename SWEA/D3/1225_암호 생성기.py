from collections import deque
for test in range(1, 11):
    t = int(input())
    data = deque(list(map(int, input().split())))
    i = 1 
    while data[-1] != 0:
        a = data.popleft() - i
        if a < 0:
            a = 0
        data.append(a)
        i = i % 5 + 1
    print("#{} {:} {:} {:} {:} {:} {:} {:} {:}".format(test, *data))