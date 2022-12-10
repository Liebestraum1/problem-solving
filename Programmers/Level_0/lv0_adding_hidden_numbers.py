#Programmers lv.0, 숨어있는 숫자의 덧셈
def solution(my_string):
    result = 0
    stack = '0'
    for v, i in enumerate(my_string, 1):
        if i in "1234567890":
            stack += i
            if v == len(my_string):
                result += int(stack)
        else:
            result += int(stack)
            stack = '0'
    return result