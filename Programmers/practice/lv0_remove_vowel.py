#Programmers lv.0, 모음 제거
def solution(my_string):
    for i in "aeiou":
        my_string = my_string.replace(i, "")
    return my_string