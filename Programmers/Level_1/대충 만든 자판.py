def solution(keymap, targets):
    keyboard = {chr(key) : 101 for key in range(65, 91)}
    answer = []
    for key in keymap:
        for cnt, string in enumerate(key, 1):
            keyboard[string] = min(keyboard[string], cnt)
    
    for target in targets:
        cnt = 0
        for string in target:
            if keyboard[string] == 101:
                cnt = -1
                break
            cnt += keyboard[string]
        answer.append(cnt)
    return answer