#Programmers lv.0, 연속된 수의 합
def solution(lines):
    def length(line1, line2):
        a = min(line1[1], line2[1]) - max(line1[0], line2[0])
        return a if a > 0 else 0
    
    if  min(lines, key = lambda x : x[1])[1] - max(lines, key = lambda x : x[0])[0] <= 0:
        a = 0
    else:
        a = min(lines, key = lambda x : x[1])[1] - max(lines, key = lambda x : x[0])[0]
    return length(lines[0], lines[1]) + length(lines[0], lines[2]) + length(lines[1], lines[2]) - a * 2