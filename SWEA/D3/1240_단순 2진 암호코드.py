t = int(input())

dic = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3,
       '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7,
       '0110111' : 8, '0001011' : 9}

for test in range(1, t+1):
    answer, s = 0, 0
    n, m = map(int, input().split())
    
    for i in range(n):
        data = list(map(int, input().split()))
        if data[-1] != 0:
            break 
        
    for i in range(0, 56, 7):
        decoding = dic[data[i:i+7]]
        s += decoding
        if i % 2:
            answer += decoding * 3
        else:
            answer += decoding

    if answer < 10 or answer % 10:
        print(f"#{test} 0")
    else:
        print(f"#{test} {s}")