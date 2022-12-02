#Programmers lv.2, JadonCase 문자열 만들기
def solution(s):
    s = " " + s
    answer = ""
    for i in range(1, len(s)):
        if s[i-1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer