#Programmers lv.1, 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return arr if arr != [] else [-1]