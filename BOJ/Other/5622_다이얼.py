word = input()
dic = {}
answer = 0
for i in range(26):
    dic[chr(i+65)] = i//3 + 2
dic['S'] = 7; dic['V'] = 8; dic['Y'] = 9; dic['Z'] = 9
for s in word:
    answer += dic[s] + 1
print(answer)