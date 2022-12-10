#프로그래머스 lv.0, 짝수는 싫어요
def solution(num, total):
    end = total // num - (num-1) // 2
    return list(range(end, end+num))