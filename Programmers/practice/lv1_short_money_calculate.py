#Programmers lv.1, 부족한 금액 계산하기
def solution(price, money, count):
    for i in range(1, count+1):
        money -= i * price
    return 0 if money >= 0 else -money