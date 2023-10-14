answer = 0
visit = set()
def DFS(cnt, target, dic, visited):
    global visit
    global answer
    
    if(cnt == target):
        visit.add(visited)
        return
    
    for choosedid in dic[cnt]:
        if(visited & (1 << choosedid) == 0):
            new_visited =  visited | (1 << choosedid)
            DFS(cnt + 1, target, dic, new_visited)
        
    
def solution(user_id, banned_id):
    global answer
    global visit
    dic = [[] for _ in range(len(banned_id))]
    answer = 0
    
    for i, bannedid in enumerate(banned_id):
        for j, userid in enumerate(user_id):
            flag = True
            if len(bannedid) != len(userid):
                flag = False
                continue
            for k in range(len(userid)):
                if(bannedid[k] == "*"):
                    continue
                if(bannedid[k] == userid[k]):
                    continue
                flag = False
            if flag == True:
                dic[i].append(j)
# 중복되는 경우를 어떻게 곱할지 생각해보자.
# 한사람은 ABC, 나머지 한사람은 BC를 고른다.
    print(dic)
    DFS(0 , len(banned_id), dic, 0)
    print(visit)
    
    return len(visit)