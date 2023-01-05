def solution(storey):
    answer = 0
    while storey > 0:
        if storey % 10 == 5:
            answer += 5
            if storey // 10 % 10 >= 5:
                storey = storey // 10 + 1
            else:
                storey = storey // 10          
        elif storey % 10 > 5:
            answer += (10 - storey % 10)
            storey = storey // 10 + 1
        else:
            answer += storey % 10
            storey = storey // 10
            
    return answer