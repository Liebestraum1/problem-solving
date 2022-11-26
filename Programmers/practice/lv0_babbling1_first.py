def solution(babbling):
    word = [] #발음 가능 단어 목록
    answer = 0 #정답
    
    #리스트의 모든 조합을 반환하는 함수
    def permutations(input_list=[], depth=[], visited=[]):
        for i in range(len(input_list)):
            tmp = depth[:]
            depth = depth + [input_list[i]]
            visited.append(depth)
            permutations(input_list[:i] + input_list[i+1:], depth, visited)
            depth = tmp
        return(visited)
    
    #단어 조합 이어붙여서 발음 가능 단어 목록에 삽입
    for i in permutations(["aya", "ye", "woo", "ma"]):
        word.append("".join(i))

    #발음 가능 단어 목록과 입력받은 목록 비교
    for i in babbling:
        if i in word:
            answer += 1
    return answer