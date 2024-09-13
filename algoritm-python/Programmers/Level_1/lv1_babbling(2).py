#Programmers lv.1, 옹알이 (2)
def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babble in babbling:
        stack1 = ""
        stack2 = ""
        for spell in babble:
            stack1 += spell
            if len(stack1) > 3 or stack1 == stack2:
                break
            if stack1 in word:
                stack2 = stack1
                stack1 = ''
        if stack1 == '':
            answer += 1
    return answer