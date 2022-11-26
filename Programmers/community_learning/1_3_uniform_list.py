def solution(n, lost, reserve):
    student = [1] * (n+2) #2를 더하는 이유는 코드 구현상의 편리함을 위함
    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1
    for i in range(1, n+1):
        if student[i] == 2 and student[i-1] == 0:
            student[i - 1: i +1] = [1, 1]
        elif student[i] == 2 and student[i+1] == 0:
            student[i: i + 2] = [1, 1]
    return len([x for x in student[1:-1] if x > 0])