def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: int((x*4)[:4]), reverse=True)
    return '0' if int(''.join(numbers)) == 0 else ''.join(numbers)