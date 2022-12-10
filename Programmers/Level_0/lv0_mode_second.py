#Programmers lv.0, 최빈값 구하기 2번 풀이
def solution(array):
    while len(array) != 0: #배열의 원소가 있을 때 순회
        for i, a in enumerate(set(array)): #각 순회마다 array를 set 자료형으로 만들어서 배열에서 중복을 제거
            array.remove(a) #원본 배열에서 a를 제거, 배열의 길이는 1 줄어듬
        if i == 0: return a #for문 순회의 i값이 0이었다면, set의 원소가 a뿐이라는 뜻으로 이것이 최빈값 
    return -1

#각 순회에서 리스트에 등장한 값들을 전부 하나씩만(set를 통해) 지우는 구조
#계속 지워서 남은 원소가 하나 뿐이면 그것이 최빈값이 됨
#아닐 경우 모든 원소가 지워진 것이고, 최빈값이 2개 이상이라는 뜻