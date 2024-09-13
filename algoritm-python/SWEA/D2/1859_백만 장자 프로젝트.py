t = int(input())
for test in range(1, t+1):
    n = int(input()) #데이터 길이
    data = list(map(int, input().split()))[::-1]
    max_price, answer = data[0], 0
    for i in range(n):
        if data[i] <= max_price:
            answer += max_price - data[i]
        else:
            max_price = data[i]
    print(f"#{test} {answer}")