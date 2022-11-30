#Programmers lv.0, 치킨 쿠폰
def solution(chicken):
    coupon = 0
    while chicken >= 10:
        coupon += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return coupon