#Programmers lv.0, 인덱스 바꾸기
def solution(my_string, num1, num2):
    return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]