#Prgorammers lv.0, 진료 순서 정하기
def solution(emergency):
    order = {b : a for a, b in enumerate(sorted(emergency, reverse=True), 1)}
    answer = [order[key] for key in emergency]
    return answer