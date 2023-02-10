#Sol. 1
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

#Sol. 2 -> .index 메소드를 뺄 방법은 없을까?
def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    answer = [alphabet[(alphabet.index(a) + index) % len(alphabet)] for a in s]
    return ''.join(answer)