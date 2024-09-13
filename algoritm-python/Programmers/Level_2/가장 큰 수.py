def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x: x*3, reverse=True)
    return '0' if int(''.join(numbers)) == 0 else ''.join(numbers)

#아스키 코드에 따라 정렬하기 때문에, line 3에서 int로 변환할 필요가 딱히 없음.