def solution(dots):
    
    def gradient(dot1, dot2):
        return (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
    
    for i in range(1, len(dots)):
        print(dots[0],dots[i])
        print(gradient(dots[0], dots[i]), gradient((dots[1:i] + dots[i+1:])[0], (dots[1:i] + dots[i+1:])[1]))
        if gradient(dots[0], dots[i]) == gradient((dots[1:i] + dots[i+1:])[0], (dots[1:i] + dots[i+1:])[1]):
            return 1
    
    return 0