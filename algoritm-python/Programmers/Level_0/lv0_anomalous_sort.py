#Programmers lv.0, 특이한 정렬
def solution(numlist, n):
    numlist.sort(key = lambda x : (abs(x-n), n-x)) #key에 튜플을 넣을 경우, 첫 번째 값이 같을 땐 두 번째 값을 기준으로 다시 정렬한다.
    return numlist