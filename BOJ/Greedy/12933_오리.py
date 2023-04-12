sound = list(input())
stack = []
duck = ['q', 'u', 'a', 'c', 'k'] #q, u, a, c, k
answer, idx = 0, 0

while len(sound) >= 5 and sound[0] == 'q':
    answer += 1
    stack = []
    for i in range(len(sound)):
        if sound[i] == duck[idx]:
            idx = (idx + 1) % 5
        else:
            stack.append(sound[i])
    sound = stack

print(-1 if sound else answer)