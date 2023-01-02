def solution(n): #반복문
    f_0, f_1 = 0, 1
    
    for _ in range(n-1):
        f_0, f_1 = f_1, f_0 + f_1
    return f_1%1234567