def solution(picks, minerals):
    end = sum(picks) * 5
    minerals_bundle = []
    answer = 0
    
    for i in range(0, end, 5): 
        if bundle := minerals[i:i+5]:
            minerals_bundle.append(bundle)
            
    minerals_bundle.sort(key = lambda x:
                         (x.count('diamond'), x.count('iron'), x.count('stone')))
    
    while minerals_bundle:
        mining = minerals_bundle.pop()
        while picks[0] == 0:
            picks.pop(0)
        picks[0] -= 1
        
        if len(picks) == 3: #diamond
            answer += len(mining)
        elif len(picks) == 2: #iron
            answer += mining.count("diamond") * 5
            answer += len(mining) - mining.count("diamond")
        else:
            answer += mining.count("diamond") * 25
            answer += mining.count("iron") * 5
            answer += mining.count("stone")           
    return answer