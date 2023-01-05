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