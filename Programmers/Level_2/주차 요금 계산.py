def solution(fees, records):
    #fees 0 기본시간 1 기본요금 2 단위시간 3 단위요금
    dic = {int(i[6:10]) : [0, 0, 0, 0] for i in records} #입차시간, 출차시간, 누적 주차시간, 출차 여부
    
    for i in records: #len(i) = 13 or 14, [:2] 시, [3:5] 분, [6:10] 번호, [11:]출입여부
        hour = int(i[:2]); minute = int(i[3:5]); number = int(i[6:10]); io = i[11:]   
        if io == 'IN':
            dic[number][0] = hour * 60 + minute
            dic[number][3] = False
        else:
            dic[number][1] = hour * 60 + minute
            dic[number][2] += dic[number][1] - dic[number][0]
            dic[number][0], dic[number][1], dic[number][3] = 0, 0, True
    
    for number in dic:
        if not dic[number][3]:
            dic[number][2] += 1439 - dic[number][0]
        
        if dic[number][2] <= fees[0]:
            dic[number] = fees[1]
        else:
            if (dic[number][2] - fees[0]) % fees[2] == 0:
                dic[number] = (dic[number][2] - fees[0]) // fees[2] * fees[3] + fees[1]
            else:
                dic[number] = ((dic[number][2] - fees[0]) // fees[2] + 1) * fees[3] + fees[1]
        
    return [item[1] for item in sorted(dic.items(), key = lambda x: x[0])]