def solution(record):
    dic = {}
    answer = []
    for log in record:
        k = log.split()
        if k[0] == 'Enter' or k[0] == 'Change':
            dic[k[1]] = k[2]

    for log in record:
        k = log.split()
        if k[0] == 'Enter':
            answer.append(f"{dic[k[1]]}님이 들어왔습니다.")
        elif k[0] == "Leave":
            answer.append(f"{dic[k[1]]}님이 나갔습니다.")
    return answer