#Prgorammers lv.1, 비밀지도
def solution(n, arr1, arr2):
    answer = []
    
    def convert(number, a = n):
        b = format(number, 'b')
        while len(b) < a:
            b = '0' + b
        return b
    
    arr1 = list(map(convert, arr1))
    arr2 = list(map(convert, arr2))
    
    for i in range(n):
        stack = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                stack += '#'
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                stack += ' '
        answer.append(stack)
    return answer