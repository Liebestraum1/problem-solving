#Programmers lv.0, 암호 해독
def solution(cipher, code):
    return cipher[code-1::code]