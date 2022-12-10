#Programmers lv.0, 외계행성의 나이
def solution(age):
    table = str.maketrans("0123456789", "abcdefghij")
    return str(age).translate(table)