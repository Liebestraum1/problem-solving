#Programmers lv.0, 외계어 사전
def solution(spell, dic):
    spell = set(spell)
    for word in dic:
        if not spell - set(word):
            return 1
    return 2