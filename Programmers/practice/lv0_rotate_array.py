#Programmers lv.0, 배열 회전시키기
def solution(numbers, direction):
    return numbers[1:] + [numbers[0]] if direction == "left" else [numbers[-1]] + numbers[:-1]