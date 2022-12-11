#프로그래머스 lv.1, 명예의 전당 (1)
def solution(k, score):
    mj = []
    result = []
    
    for i in score:
        mj.append(i)
        if (len(mj) > k):
            mj.remove(min(mj))
        result.append(min(mj))
    return result