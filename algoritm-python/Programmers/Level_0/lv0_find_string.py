#Programmers lv.0, 문자열 찾기2
def solution(A, B):
    for i in range(len(A)):
        if A[len(A)-i:] + A[:len(A)-i] == B:
            return i
    return -1