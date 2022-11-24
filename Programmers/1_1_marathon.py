#Hash algorithm
def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
        #dictionary.get(x, y)는 키값 x에 해당하는 value를 가져오고, 해당 key값에 대응하는 value가 없으면 y를 반환한다.
        #즉, 처음 이름이 입력될 때는 value가 없기 때문에 0이 할당되고, 이후에는 1씩 더해진다.
        #participant의 길이에 비례하는 시간 복잡도를 가진다.
    for x in completion:
        d[x] -= 1
        #completion의 길이에 비례하는 시간 복잡도를 가진다."
    dnf = [k for k, v in d.items() if v > 0]
        #dictionary.items()는 key와 value의 쌍을 반환한다
        #d의 길이에 비례하는 시간 복잡도를 가진다.
    answer = dnf[0] #완주하지 못한 선수가 1명이므로 첫번째 원소를 반환한다.
    return answer