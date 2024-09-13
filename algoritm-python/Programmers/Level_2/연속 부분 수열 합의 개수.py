def solution(elements):
    answer = set()
    elements = elements * 2
    for i in range(len(elements)//2):
        for j in range(i+1, i+1+len(elements)//2):
            answer.add(sum(elements[i:j]))
    return len(answer)