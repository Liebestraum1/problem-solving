#Programmers lv.0, 옹알이 (1) 2번 풀이

def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b: #이 조건이 없으면 중복순열을 허용함
                b = b.replace(w, ' ') #발음 가능한 단어는 공백으로 변경
        if len(b.strip()) == 0: #단어가 공백이 아닐 경우 - 발음 불가능 단어가 존재할 경우
            c += 1 #원소 수 하나 증가
    return c