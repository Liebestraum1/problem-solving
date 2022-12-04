#Programmers lv.2, 우박수열 정적분
def solution(k, ranges):
    height = [k]
    answer = []
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        height.append(k)
    
    def integral(func):
        area = 0.0
        for i in range(len(func)-1):
            area += (func[i] + func[i+1]) / 2
        return area
    
    for i, (x1, x2) in enumerate(ranges):
        ranges[i] = (x1, len(height) + x2)
    
    for x1, x2 in ranges:
        if x1 >= x2:
            answer.append(-1.0)
        else:
            answer.append(integral(height[x1:x2]))
    
    return answer