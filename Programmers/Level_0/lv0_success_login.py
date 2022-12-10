#Programmers lv.0, 로그인 성공?
def solution(id_pw, db):
    db = {i : v for i, v in db}
    
    if id_pw[0] in db and id_pw[1] == db[id_pw[0]]:
        return "login"
    elif id_pw[0] in db and id_pw[1] != db[id_pw[0]]:
        return "wrong pw"
    elif id_pw[0] not in db:
        return "fail"