#Programmers lv.1 신고 결과 받기
def solution(id_list, report, k):
    report = set(report) #중복 신고 제거
    reporting_dict = {i: [] for i in id_list} #각 유저가 신고한 유저들을 리스트로 보여주는 딕셔너리
    reported_count = {} #각 유저별로 신고당한 회수를 보여주는 딕셔너리
    mail = [0] * len(id_list)

    for i in report:
        reporting_dict[i.split()[0]].append(i.split(" ")[1])
    
    for id in [reported_id.split()[1] for reported_id in report]: #report에서 신고당한 아이디만 보여줌
        reported_count[id] = reported_count.get(id, 0) + 1
        
    for i, j in enumerate(id_list):
        for reported_id in reporting_dict[j]:
            if reported_count[reported_id] >= k:
                mail[i] += 1
                
    return mail
