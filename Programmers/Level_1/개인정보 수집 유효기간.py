def solution(today, terms, privacies):
    answer = []
    t = today.split('.')
    today = int(t[0][2:]) * 28 * 12 + int(t[1]) * 28 + int(t[2])
    
    due = {}
    for term in terms:
        due[term.split()[0]] = int(term.split()[1]) * 28    
    
    for i, p in enumerate(privacies, 1):
        d = p.split()[0].split('.')
        day = int(d[0][2:]) * 28 * 12 + int(d[1]) * 28 + int(d[2])
        if today - day >= due[p.split()[1]]:
            answer.append(i)
    return answer