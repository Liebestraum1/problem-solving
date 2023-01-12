#그리디 5. 볼링공 고르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
count = [0] * 11
answer = 0

for weight in data:
    count[weight] += 1

for i in range(1, m + 1):
    n -= count[i]
    answer += count[i] * n
    
print(answer)

#서로 다른 무게를 가진 공을 고르고 싶다.
#공의 번호가 달라도 무게가 같을 수 있다.
#A가 무게가 1인 공을 고른다.
#B는 나머지 4개의 볼을 선택할 수 있다.

#A가 무게가 2인 공을 고른다.
#B는 2개의 공을 선택할 수 있다

#A가 무게가 3인 공을 고른다. -> 불가
