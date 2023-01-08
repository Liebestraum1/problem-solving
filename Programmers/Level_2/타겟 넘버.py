def solution(numbers, target):
    stack = [0]
    while numbers != []:
        answer = []
        number = numbers.pop()
        for i in stack:
            answer.append(i - number)
            answer.append(i + number)
        stack = answer[:]
    return answer.count(target)

def solution(numbers, target): #재귀를 이용한 풀이
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])