#Programmers lv.0, 영어가 싫어요
def solution(numbers):
    n = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
    for i, v in enumerate(n):
        numbers = numbers.replace(v, str(i))
    return int(numbers)