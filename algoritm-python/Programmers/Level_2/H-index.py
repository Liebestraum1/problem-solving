def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i in citations:
        if i > h:
            h += 1
    return h