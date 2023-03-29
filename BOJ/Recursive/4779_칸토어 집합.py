import sys

def cantor(string):
    if string.strip() == '' or string == '-':
        return string
    return cantor(string[:len(string)//3]) + cantor(' ' * (len(string)//3)) + cantor(string[:len(string)//3])

for line in sys.stdin:
    n = int(line)
    data = '-' * 3 ** n
    print(cantor(data))