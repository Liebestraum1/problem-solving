#Programmers lv.1, 키패드 누르기
def solution(numbers, hand):
    #2580에서의 거리 계산 (편의상 별은 10, 0은 11, 샵은 12로 바꿈)
    #두 수를 빼서 3으로 나눈 몫에 나머지를 더한게 거리
    answer = ''
    lt = 10
    rt = 12
    numbers = [i + 11 if i == 0 else i for i in numbers]
    
    def distance(n1, n2):        
        return sum(divmod(abs(n1 - n2),3))
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            lt = i
        elif i in [3, 6, 9]:
            answer += "R"
            rt = i
        else:
            if distance(lt, i) < distance(rt, i):
                answer += "L"
                lt = i
            elif distance(lt, i) > distance(rt, i):
                answer += "R"
                rt = i
            else:
                if hand == "right":
                    answer += "R"
                    rt = i
                elif hand == "left":
                    answer += "L"
                    lt = i
    return answer