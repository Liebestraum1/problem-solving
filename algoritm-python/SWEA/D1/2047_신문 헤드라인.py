t = input()
answer = ""
for s in t:
    if ord(s) >= 97 and ord(s) <= 122:
        answer += chr(ord(s) - 32)
    else:
        answer += s
print(answer)