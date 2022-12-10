#Programmers lv.0, 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    return sum([int(i) for i in my_string if i in "1234567890"])