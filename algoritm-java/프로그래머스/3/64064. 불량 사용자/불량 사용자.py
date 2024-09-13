visit = set()
def DFS(cnt, target, dic, visited):
    global visit
    
    if(cnt == target):
        visit.add(visited)
        return
    
    for choosedid in dic[cnt]:
        if(visited & (1 << choosedid) == 0):
            new_visited =  visited | (1 << choosedid)
            DFS(cnt + 1, target, dic, new_visited)
        
    
def solution(user_id, banned_id):
    global visit
    dic = [[] for _ in range(len(banned_id))]
    
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

    DFS(0 , len(banned_id), dic, 0)
    return len(visit)