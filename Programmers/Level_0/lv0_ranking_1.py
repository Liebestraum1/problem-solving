#Programmers lv0. 등수 매기기
def solution(score):
    avr = [[(i + v), 1] for i, v in score]
    for i in range(len(avr)):
        avr = [[a, b+1] if a < avr[i][0] else [a, b] for a, b in avr] 
    return [j[1] for j in avr]