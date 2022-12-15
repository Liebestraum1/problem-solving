#Programmers lv.1, 신규 아이디 추천
def solution(new_id):
    new_id = new_id.lower() #1
    recommend = "."
    
    for c in new_id: #2
        if c.isdigit() or c.islower() or c in ['-', '_']:
            recommend += c
        if c == '.' and recommend[-1] != '.': #3
            recommend += c
    
    recommend = recommend.strip('.') #4
    
    if recommend == "": #5
        recommend = "a"
    
    recommend = recommend[:15].rstrip('.') #6
    
    while len(recommend) < 3: #7
        recommend += recommend[-1]
    
    return recommend