#Programmers lv.1, 폰켓몬
def solution(nums):
    a = len(set(nums))
    if len(nums) // 2 >= a:
        return a
    else:
        return len(nums) // 2