def solution(n, lost, reserve):
    student = [1] * (n + 2) # +2를 하는 이유는 코드 작성의 편의를 위함
    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1
    for i in range(1, n+2):
        if student[i] == 2 and student[i-1] == 0:
            student[i] = 1
            student[i-1] = 1
        elif student[i] == 2 and student[i+1] == 0:
            student[i] = 1
            student[i+1] = 1
    return student.count(1) + student.count(2) - 2

