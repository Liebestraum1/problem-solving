def solution(k, tangerine):
    dic = {}
    
    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    
    a = sorted(list(dic.items()), key = lambda x: x[1])
    cnt = len(tangerine)
    
    for key, value in a:
        if k <= cnt - value:
            cnt -= value
            dic.pop(key)
    
    return len(dic)