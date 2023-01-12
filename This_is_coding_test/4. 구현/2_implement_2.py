#행위치 1 ~ 8
#열위치 a ~ h
data = input()
result = 0
l = [ord(data[0]) - 96, int(data[1])]

if l[0] + 2 < 9 and l[1] + 1 < 9:
    result += 1
if l[0] + 1 < 9 and l[1] + 2 < 9:
    result += 1
if l[0] - 2 > 0 and l[1] - 1 > 0:
    result += 1
if l[0] - 1 > 0 and l[1] - 2 > 0:
    result += 1
if l[0] + 2 < 9 and l[1] - 1 > 0:
    result += 1
if l[0] + 1 < 9 and l[1] - 2 > 0:
    result += 1
if l[0] - 2 > 0 and l[1] + 1 < 9:
    result += 1
if l[0] - 1 > 0 and l[1] + 2 < 9:
    result += 1

print(result)