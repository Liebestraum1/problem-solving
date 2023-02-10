def solution(s, skip, index):
    answer = ''
    for alphabet in s:
        a = ord(alphabet)
        for _ in range(index):
            a += 1
            while r(a) in skip:
                a += 1
        answer += r(a)
    return answer

def r(a : int):
    return chr((a - 97) % 26 + 97)